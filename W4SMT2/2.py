class Shinobi: 
    GENIN, CHUNIN, JOUNIN = range(3) 
    def __init__(self, nama, rank): 
        self.nama = nama 
        self.rank = rank 
        
    def status_ujian(self): 
        if self.rank < 1: 
            print(self.nama, "boleh ikut ujian") 
        else: 
            print(self.nama, "tidak boleh ujian") 
#Contoh pembuatan objek 
ninja1 = Shinobi("Naruto", Shinobi.GENIN) 
ninja1.status_ujian()

class Clan(Shinobi): 
    def __init__(self, clan, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.clan = clan 
        self.nama = " ".join([self.clan, self.nama]) 
ninja2 = Clan("Uchiha", "Sasuke", Shinobi.GENIN) 
ninja2.status_ujian()