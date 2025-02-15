NIU = int(input('Masukkan NIU (Hanya 6 digit): '))
Tugas = float(input('Masukkan nilai tugas: '))
Laporan = float(input('masukkan nilai laporan: '))
average = (Tugas + Laporan) / 2
while True:
    if average <40:
        print('Nilai yang didapat: K')
        break
    Nilai_Ujian = float(input('Masukkan nilai ujian: '))
    nilai_akhir = Tugas * 0.25 + Laporan * 0.25 + Nilai_Ujian*0.5
    if nilai_akhir <=100 and nilai_akhir>=80:
        print('Nilai yang didapat: A')
        break
    elif nilai_akhir <80 and nilai_akhir>=70:
        print('Nilai yang didapat: B')
        break
    if nilai_akhir <70 and nilai_akhir>=60:
        print('Nilai yang didapat: C')
        break
    if nilai_akhir <60 and nilai_akhir>=50:
        print('Nilai yang didapat: D')
        break
    else:
        print('Nilai yang didapat: E')
        break