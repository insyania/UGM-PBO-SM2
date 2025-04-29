from collections import namedtuple
class Orang (namedtuple("Orang", "nama anak")) :
    def tampilkan_info (cls) :
        def tampilkan_info(self):
            print("Nama : ", self.nama)
            print("Nama anak : ")
            for i in range(len(self.anak)):
                print (f"{i+1}. {self.anak[i]}")
        cls.info = tampilkan_info
        return cls
    
    @tampilkan_info
    class MyClass :
        pass

john = Orang("John Doe", ["Timmy", "Jimmy"])
print(john)
print(id(john.anak))

john.anak.append("Tina")
print(john)
print(id(john.anak))

john.tampilkan_info()