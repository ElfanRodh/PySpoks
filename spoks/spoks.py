import json
import os
import sys

class Spoks(object):
    def __init__(self):
        self.current_dir = os.path.dirname(os.path.realpath(__file__))
        self.maks = 5

    def unique(self, list1): 
        h = []
        
        list_set = set(list1) 
        unique_list = (list(list_set)) 
        for x in unique_list: 
            h.append(x)
        
        return h
        
    def preproses(self, cont):
        dictionaryFile = self.current_dir + '/data/adjective.json'
        file = dictionaryFile

        with open(file) as g:
            fil = json.load(g)
            
        pre = {}
        hasil = []
        hasilnya = {}

        # CASE FOLDING
        casefold = cont.casefold()
        replaceku = ['.',',','/','\\','+','(',')','@','!','~','`','#','$','%','^','&','*','=',':',';','?','<','>']

        for elem in replaceku :
            if elem in casefold :
                casefold = casefold.replace(elem, '')

        # TOKENIZING PAKAI CORPUS
        tokens = casefold.split()
        
        #  PASSLIST KATA SIFAT
        for katas in fil:
            for token in tokens:
                if token in katas['synset'].split(','):
                    hasil.append(token)
        h = self.unique(hasil);
        
        hasilnya['hasil'] = h

        pre['cf'] = casefold
        pre['hasil'] = hasilnya
        
        return pre

    def input_kategori(self, kat):
        dictionaryFile = self.current_dir + '/data/kategori.json'
        file = dictionaryFile
        kategori = [[0 for x in range(len(kat))] for x in range(len(kat))]

        if os.stat(file).st_size > 0:
            f = open(file, 'r+')
            f.truncate(0)

        for i in range(len(kat)):
            kategori[i] = {"kategori" : kat[i]}

        with open(file, 'r+') as outfile:  
            json.dump(kategori, outfile)
            outfile.close()
        
        return kategori

    def input_sub(self, kategori, asp):
        dictionaryFile = self.current_dir + '/data/kategori.json'
        file = dictionaryFile
        
        with open(file, 'r') as outfile: 
            data = json.load(outfile)
        
        print(data)
        
        for z in range(len(data)):
            print()
            if data[z]['kategori'] == kategori:
                data[z]['sub_kategori'] = []
                for a in range(len(asp)):
                    data[z]["sub_kategori"].append({
                        "nama_sub" : asp[a]
                    })
                    
        print(data)
        
        with open(file, 'w') as outfile:  
            json.dump(data, outfile)
            outfile.close()
            
        return data

    def show_kategori(self):
        kt = self.current_dir + '/data/kategori.json'

        with open(kt) as f:
            aspek = json.load(f)

        return aspek

    def spoks(self, hasil):
        kt = self.current_dir + '/data/kategori.json'
        ad = self.current_dir + '/data/adjective.json'

        with open(kt) as f:
            aspek = json.load(f)

        with open(ad) as g:
            sif = json.load(g)
        
        ret = {}
        sis = {}
        th = {}
        jum = {}
        syn_ = {}
        ant_ = {}
        c = {}
        jumlah = {}
        avg = {}
        # maks = self.maks
        cr = {}
        
        for asp in aspek:
            sis[asp['kategori']] = {}
            th[asp['kategori']] = {}
            jum[asp['kategori']] = {}
            syn_[asp['kategori']] = {}
            ant_[asp['kategori']] = {}
            c[asp['kategori']] = 0
            jumlah[asp['kategori']] = 0
            avg[asp['kategori']] = 0
            
            for sub in asp['sub_kategori']:

                jum[asp['kategori']][sub['nama_sub']] = 0

                for adj in sif:

                    if sub['nama_sub'] in adj['synset'].split(','):

                        syn_[asp['kategori']][sub['nama_sub']] = adj['synset'].split(',')
                        ant_[asp['kategori']][sub['nama_sub']] = adj['antset'].split(',')

                        for has in hasil['hasil']:
                            if has==sub['nama_sub']:
                                jum[asp['kategori']][sub['nama_sub']] = jum[asp['kategori']][sub['nama_sub']]+1

                            for synset in syn_[asp['kategori']][sub['nama_sub']]:
                                if has == synset:
                                    jum[asp['kategori']][sub['nama_sub']] = jum[asp['kategori']][sub['nama_sub']]+1

                            for antset in ant_[asp['kategori']][sub['nama_sub']]:
                                if has == antset:
                                    jum[asp['kategori']][sub['nama_sub']] = jum[asp['kategori']][sub['nama_sub']]-1

                #SC Val
                sc = jum[asp['kategori']][sub['nama_sub']]
                sis[asp['kategori']][sub['nama_sub']] = sc
                print('Nama Kategori : '+str(asp['kategori']))
                print('SC Val '+sub['nama_sub']+' : '+str(sc))

                #TH
                if sc >= 1:
                    th[asp['kategori']][sub['nama_sub']] = 1
                if sc < 0:
                    th[asp['kategori']][sub['nama_sub']] = -1
                if sc == 0:
                    th[asp['kategori']][sub['nama_sub']] = 0
                
                print('TH '+str(asp['kategori'])+' : '+str(th[asp['kategori']][sub['nama_sub']]))

                #C
                c[asp['kategori']] = c[asp['kategori']] + th[asp['kategori']][sub['nama_sub']]
                print('C '+str(asp['kategori'])+' : '+str(c[asp['kategori']]))

                #Average
                jumlah[asp['kategori']] = len(asp['sub_kategori'])
                avg[asp['kategori']] = c[asp['kategori']]/jumlah[asp['kategori']]
                print('Jumlah '+str(asp['kategori'])+' : '+str(jumlah[asp['kategori']]))

                print('AVG '+str(asp['kategori'])+' : '+str(avg[asp['kategori']]))
            
        #CR
        cx = 0
        for avgs in aspek:
            cr[avgs['kategori']] = avg[avgs['kategori']] * self.maks
            print('CRR : '+str(cr[avgs['kategori']]))
            
            cx = cx+cr[avgs['kategori']]
        
        print('CR : '+str(cx))

        # RATING
        fr = cx/len(aspek)
        print('Rating : '+str(fr))

        # END COMMENT
        
        ret['scv'] = sis
        ret['th'] = th
        ret['c'] = c
        ret['avg'] = avg
        ret['cr'] = cr
        ret['fr'] = fr
        ret['aspek'] = aspek

        print(sis)

        return ret