Python SPOKS
===============

Library Sistem Pemeringkat Otomatis Berbasis Kata Sifat untuk Bahasa Perograman Python

Cara Install
-------------

PySpoks dapat di-*install* menggunakan [pip](https://docs.python.org/3.6/installing/index.html), dengan menjalankan perintah berikut di terminal/command prompt : `pip install PySpoks`

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

Lisensi
-----------

Lisensi PySastrawi adalah MIT License (MIT).

Project ini mengandungTesaurus Bahasa Indonesia dari KBBI
