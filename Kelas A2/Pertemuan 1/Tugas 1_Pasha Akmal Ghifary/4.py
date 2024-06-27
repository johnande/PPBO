def cek_prima(angka):
    if angka > 1:
        for i in range(2, int(angka**0.5) + 1):
            if angka % i == 0:
                return False
        return True
    else:
        return False


angka = int(input("Masukkan angka: "))
if cek_prima(angka):
    print("Angka prima")
else:
    print("Bukan angka prima")

