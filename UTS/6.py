class Rekening :
    def __init__(self, Nama, rekeningnum, saldo ):
        self. Nama = Nama
        self.rekeningnum = rekeningnum
        self.saldo = saldo

    def setor_tunai (self, saldo, nominal):
        self.nominal = nominal
        self.saldo = saldo + nominal

    def tarik_tunai (self, saldo, nominal) :
        self.nominal = nominal
        self.saldo = saldo - nominal

    def transfer (self, penerima, nominal):
        self.saldo -= nominal
        penerima.saldo += nominal
        print('transfer dengan nominal : ', nominal, 'dari rekening ', self.rekeningnum, 'menuju rekening ', penerima.rekeningnum, 'berhasil')

        
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
print()
pengguna1.setor_tunai(500000, 1000000)
pengguna2.tarik_tunai(2000000, 1000000)
print('Data setelah transaksi dilakukan:')
print('Nasabah 1')
pengguna1.show_data()
print()
print('Nasabah 2')
pengguna2.show_data()
print()
pengguna1.transfer(pengguna2, 500000)
print()
print('data nasabah setelah transaksi dilakukan')
pengguna1.show_data()
print()
pengguna2.show_data()
print()