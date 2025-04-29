#namedtupple
from collections import namedtuple
Koordinat = namedtuple ('Koordinat', ['x', 'y'])
titik1 = Koordinat ('2','4')

#tupplebiasa
koor = (2, 3)
Koordinat = namedtuple ('Koordinat', 'x y')
titik1 = Koordinat (x = '2', y = '4')

#akses elemen menggunakan indeks
print ('X : ', titik1[0])
#akses elemen menggunakan nama atribut
print('X : ', titik1.x)
#akese menggunakan getattr
print('X : ', getattr(titik1, 'x'))

#akses elemen menggunakan indeks
print ('Y : ', titik1[1])
#akses elemen menggunakan nama atribut
print('Y : ', titik1.y)
#akese menggunakan getattr
print('Y : ', getattr(titik1, 'y'))
