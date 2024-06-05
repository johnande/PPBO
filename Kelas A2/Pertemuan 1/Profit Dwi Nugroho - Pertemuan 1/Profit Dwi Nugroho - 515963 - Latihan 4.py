def cek_prima(angka):
    if angka <= 1:
        return False
    elif angka == 2:
        return True
    elif angka % 2 == 0:
        return False
    else:
        batas = int(angka**0.5) + 1
        for i in range(3, batas, 2):
            if angka % i == 0:
                return False
        return True

# Input angka dari pengguna
angka_input = int(input("Masukkan angka: "))

# Memeriksa apakah angka tersebut prima atau tidak
if cek_prima(angka_input):
    print(f"{angka_input} adalah angka prima")
else:
    print(f"{angka_input} bukan angka prima")