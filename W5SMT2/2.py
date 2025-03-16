class Makanan: 
    def intro(self): 
        print("Makanan pokok apa yang jadi kesukaanmu?") 
        
    def menu(self): 
        print("Makanan pokok yang banyak di konsumsi masyarakat adalah roti (gandum) dan nasi (beras)") 
        
class Eropa(Makanan): 
    def menu(self):
        print("Makanan pokok di Eropa adalah roti (gandum)") 
        
class Asia(Makanan): 
    def menu(self): 
        print("Makanan pokok di Asia adalah nasi (beras)")

food = Makanan()
nasi = Asia()
roti = Eropa()

food.intro()
food.menu()
nasi.menu()
roti.menu()