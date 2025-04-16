class Rekening :
    def __init__(self, Nama, rekeningnum, saldo ):
        self. Nama = Nama
        self.rekeningnum = rekeningnum
        self.saldo = saldo

class Nasabah(Rekening):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def show_data (self):
        print('Nama     : ', self.Nama)
        print('Rekening : ', int(self.rekeningnum))
        print('Saldo    : ', float(self.saldo))

pengguna1 = Nasabah('Budi', 5555, 500000)      
pengguna2 = Nasabah('Wati', 6666, 2000000)
print('Nasabah 1')
pengguna1.show_data()
print()
print('Nasabah 2')
pengguna2.show_data()