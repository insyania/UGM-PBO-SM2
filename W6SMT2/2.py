from abc import ABC, abstractmethod 
class Bangundatar(ABC): 
    
    @abstractmethod 
    def luas(self): 
        pass 
    @abstractmethod 
    def keliling(self): 
        pass 

class Persegi(Bangundatar): 
    nama = "Persegi" 
    def __init__(self, panjang_sisi): 
        self.panjang_sisi = panjang_sisi 
    def luas(self): 
        return self.panjang_sisi ** 2 
    def keliling(self): 
        return self.panjang_sisi * 4
class Persegipanjang(Bangundatar): 
    nama = "Persegi Panjang" 
    def __init__(self, panjang, lebar): 
        self.panjang = panjang 
        self.lebar = lebar 
    def luas(self): 
        return self.panjang * self.lebar 
    def keliling(self): return 2 * (self.panjang + self.lebar) 

p = Persegi(5) 
pp = Persegipanjang(4, 5) 
for i in (p, pp): 
    print("Luas", i.nama, i.luas()) 
    print("Keliling", i.nama, i.keliling())