from collections import namedtuple
Kendaraan = namedtuple ('Platnomor', ['Kota', 'Kode'])

kdr1 = Kendaraan ('Jogja', 'AB')
kdr2 = Kendaraan ("Medan", 'BK')
kdr3 = Kendaraan ('Bandung', 'D')

print ('Kota : ', kdr1.Kota)
print ('Kode : ', getattr(kdr1, 'Kode'))
print ('Kota : ', kdr2.Kota)
print ('Kode : ', getattr(kdr2, 'Kode'))
print ('Kota : ', kdr3.Kota)
print ('Kode : ', getattr(kdr3, 'Kode'))