class Pasien :
    jumlah_pasien = 0
    def __init__ (self, nama, kelas, poli, ruang):
        self.nama = nama
        self.kelas = kelas
        self.poli = poli
        self.ruang = ruang
    
    @classmethod
    def kelas (cls) :
        return cls.kelas
    
    @staticmethod
    def poli (self) :
        return Pasien.poli
    
    @property
    def ruang_kosong (self):
        ruang_terpakai = 3
        return self.ruang - ruang_terpakai

    def tampilkan_info (cls) :
        def tampilkan_info(self):
            print("Nama : ", self.nama)
        
        cls.info = tampilkan_info
        return cls
    
    @tampilkan_info
    class Pasien :
        pass
    
pasien1 = Pasien ('Budi', 'VIP', 'Jantung', 4 )
print(pasien1.tampilkan_info)
    

    