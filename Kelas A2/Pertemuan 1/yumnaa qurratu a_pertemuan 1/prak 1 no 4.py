def cek_prima(angka):
    if angka > 1:
        for i in range(2, int(angka/2) + 1):
            if (angka % i) == 0:
                return False
        else:
            return True
    else:
        return False

# Input dari pengguna
angka_input = int(input("Masukkan angka: "))

# Memeriksa apakah angka_input adalah angka prima atau bukan
if cek_prima(angka_input):
    print(f"{angka_input} adalah angka prima")
else:
    print(f"{angka_input} bukan angka prima")

