def cek_prima(angka):
    if angka < 2:
        return False
    elif angka == 2:
        return True
    else:
        for i in range(2, int(angka**0.5) + 1):
            if angka % i == 0:
                return False
        return True

angka = int(input("Masukkan bilangan: "))

if cek_prima(angka):
    print(angka, "adalah bilangan prima")
else:
    print(angka, "bukan bilangan prima")