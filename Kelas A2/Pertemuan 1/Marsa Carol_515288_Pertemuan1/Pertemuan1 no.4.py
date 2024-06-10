def cek_bilangan_prima(angka):
    if angka <= 1:
        return False
    for i in range(2, int(angka ** 0.5) + 1):
        if angka % i == 0:
            return False
    return True

try:
    angka = int(input("Masukkan angka: "))
    if cek_bilangan_prima(angka):
        print("Angka prima")
    else:
        print("Bukan angka prima")
except ValueError:
    print("Input yang dimasukkan bukan angka.")

