from abc import ABC, abstractmethod
class jalur_transportasi (ABC) :
    def show_data (self):
        print(self.jalur(), 'dan', self.risk())

    @abstractmethod
    def jalur (self):
        pass

    @abstractmethod 
    def risk (self):
        pass

class pesawat(jalur_transportasi):
    def jalur (self):
        return('pesawat menggunakan jalur udara')
    def risk (self) :
        return('kecelakaan pesawat jarang terjadi, sehingga kategorinya aman')

class mobil(jalur_transportasi) :
    def jalur (self):
        return ('mobil menggunakan jalur darat')
    def risk (self) :
        return('kecelakaan mobil cukup sering terjadi')

class kapal(jalur_transportasi) :
    def jalur (self):
        return('kapal menggunakan jalur laut')
    def risk (self) :
        return('kecelakaan kapal cukup relatif sering terjadi')

dar = mobil()
uda = pesawat()
laut = kapal()

for kendaraan in (dar, laut, uda) :
    kendaraan.show_data() 