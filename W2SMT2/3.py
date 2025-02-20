class persegi :
    def __init__(self,sisi):
        self.sisi = sisi
    
    def keliling (self):
        return self.sisi * 4
    
    def luas(self):
        return self.sisi **2
    
if __name__ == '__main__':
    side = 45
    rectangle = persegi(side)

print('Keliling persegi = ', rectangle.keliling())
print('Luas persegi = ', rectangle.luas())
