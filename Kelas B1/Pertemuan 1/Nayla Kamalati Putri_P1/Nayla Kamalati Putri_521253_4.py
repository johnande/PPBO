#No4

def adalah_prima(angka):
    if angka <= 1:
        return False
    for i in range(2, int(angka**0.5) + 1):
        if angka % i == 0:
            return False
    return True

input_angka = input("Masukkan angka: ")
if input_angka.isdigit():
    angka = int(input_angka)
    if adalah_prima(angka):
        print(f"{angka} adalah angka prima.")
    else:
        print(f"{angka} bukan angka prima.")
else:
    print("Input harus berupa angka.")