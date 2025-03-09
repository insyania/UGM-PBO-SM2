class Orang :
    def __init__ (self, firstname, lastname, id) :
        self.firstname = firstname
        self.lastname = lastname
        self.id = id

class Mahasiswa (Orang):
    def __init__ (self, jenjang, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.jenjang = jenjang
        self.matkul = []

    SARJANA, MASTER, DOKTOR = range(3)

    def enrol (self, matakuliahh) :
        self.matkul.append(matakuliahh)

class Karyawan (Orang) :
    def __init__ (self, status, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        self.status = status

    TETAP, TDK_TETAP = range(2)

class Dosen (Karyawan) :
    def __init__ (self, *args, **kwargs) :
        super().__init__ (*args, **kwargs)
        self.matkul_diajar = []

    def mengajar (self, matakuliah) :
        self.matkul_diajar.append(matakuliah)
        
bowo = Mahasiswa ('BOWO', 'NUGROHO', 987654, Mahasiswa.SARJANA)
bowo.enrol ("Basis Data")

rizki = Dosen ('RIZKI', 'SETIABUDI', 456789, Dosen.TETAP)
rizki.mengajar ('Statistik')

class Pelajar :
    def __init__ (self) :
        self.matkul = []

    def enrol (self, matakuliah) :
        self.matkul.append(matakuliah)

class Pengajar :
    def __init__ (self) :
        self.matkul_diajar = []

    def mengajar (self, matakuliah2) :
        self.matkul_diajar.append(matakuliah2)
        
class Asdos (Orang, Pelajar, Pengajar) :
    def __init__ (self, firstname, lastname, id, ) :
        Orang.__init__ (self, firstname, lastname, id)
        Pelajar.__init__ (self)
        Pengajar.__init__ (self)

uswatun = Asdos('USWATUN', 'HASANAH', 456456)
uswatun.enrol("Big Data")
uswatun.mengajar('Kecerdasan Artifisial')
    
print(f"Mahasiswa: {bowo.firstname} {bowo.lastname}, Jenjang: {bowo.jenjang}, Matkul: {bowo.matkul}")
print(f"Dosen: {rizki.firstname} {rizki.lastname}, Status: {rizki.status}, Matkul diajar: {rizki.matkul_diajar}")
print(f"Asdos: {uswatun.firstname} {uswatun.lastname}, Matkul diambil: {uswatun.matkul}, Matkul diajar: {uswatun.matkul_diajar}")
