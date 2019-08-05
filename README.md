Python SPOKS
===============

Library Sistem Pemeringkat Otomatis Berbasis Kata Sifat untuk Bahasa Pemrograman Python

Cara Install
-------------

PySpoks dapat di-*install* menggunakan [pip](https://docs.python.org/3.6/installing/index.html), dengan menjalankan perintah berikut di terminal/command prompt : 
`pip install PySpoks`

Penggunaan
-----------

Jalankan baris-baris kode berikut di *Python interactive terminal* :

```python
# import class
import spoks

# create objek
spoks = spoks.Spoks()

# preprocess text
sentence = 'Indonesia adalah negara yang luas, indah dan sejuk. Selain itu masyarakatnya ramah'
output   = spoks.preproses(sentence)

print(output)
# {hasil : ['sejuk', 'luas', 'indah', 'ramah']}

# add kategori peratingan
kategori = ['Kualitas', 'Harga']
kat_in = spoks.input_kategori(kategori)

# add sub kategori peratingan
subs = ['bagus', 'menarik', 'kreatif']
sub_in = spoks.input_sub('Kualitas', subs)

# pemeringkat otomatis
output = spoks.preproses(sentence)
rat = spoks.spoks(output['hasil'])

print(rat)
# 'scv' = Nilai tiap Sub Kategori
# 'c'   = Nilai tiap Kategori
# 'avg' = Rata-rata Nilai Kategori
# 'cr'  = Rating Kategori
# 'fr'  = Final Rating / Rating Keseluruhan
# 'aspek' = Kategori Penilaian

```

Lisensi
--------

Lisensi PySpoks adalah MIT License (MIT).

Project ini mengandung lemma kata sifat Bahasa Indonesia dari Tesaurus Bahasa Indonesia
<<<<<<< HEAD

[Github-PySpoks](https://github.com/ElfanRodh/PySpoks)
=======
>>>>>>> c0e87457ce607e58d0a2a0bcad6975d9ff969027
