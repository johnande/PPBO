def cek_prima(angka):
    if angka <= 1:
        return False
    for i in range(2, int(angka ** 0.5) + 1):
        if angka % i == 0:
            return False
    return True

# Membaca input dari pengguna
angka = int(input("Masukkan angka: "))

# Memeriksa apakah angka adalah bilangan prima atau bukan
if cek_prima(angka):
    print(angka, "adalah bilangan prima")
else:
    print(angka, "bukan bilangan prima")
