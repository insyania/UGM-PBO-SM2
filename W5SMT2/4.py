class kecepatan :
    def __init__ (self, jarak) :
        self.jarak = jarak
    
    def __div__ (self, waktu):
        self.waktu = waktu
        return self.jarak / self.waktu
    
jar = 50000   
wak = 3400
print ('Kecepatan yang diperoleh adalah : ', jar / wak)