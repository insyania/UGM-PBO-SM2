class manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def hasil (self):
        print('Nama: ', self.nama)
        print('Umur: ', self.umur, 'tahun')

def main():
    Nama = (input('Masukkan nama: '))
    Umur = (int(input('Masukkan umur: ')))

    Manusia = manusia(Nama, Umur)
    Manusia.hasil()

if __name__ == '__main__':
    main()



