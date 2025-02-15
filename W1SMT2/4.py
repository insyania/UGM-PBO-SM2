angka = int(input('Masukkan sebuah bilangan: '))
def bil_prima(a):
    if a<2:
        return False
    for i in range (2, int(a**0.5)+1):
        if a % i ==0:
            return False
    return True
if bil_prima(angka):
    print("Bilngan Prima")
else:
    print('Bukan Bilangan Prima')