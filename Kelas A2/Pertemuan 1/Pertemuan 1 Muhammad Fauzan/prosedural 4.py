def cek_angka_primer(angka):
    if angka <= 1:
        return False
    elif angka == 2:
        return True
    elif angka % 2 == 0:
        return False
    else:
        for i in range(3, int(angka**0.5) + 1, 2):
            if angka % i == 0:
                return False
        return True

input_angka = int(input("Masukkan angka: "))

if cek_angka_primer(input_angka):
    print(f"{input_angka} adalah angka primer.")
else:
    print(f"{input_angka} bukan angka primer.")
