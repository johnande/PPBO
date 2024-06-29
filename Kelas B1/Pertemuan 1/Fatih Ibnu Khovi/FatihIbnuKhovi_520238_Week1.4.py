def angka_prima(angka):
    if angka <= 1:
        return False
    for i in range(2, (angka // 2 + 1)):
        if angka % i == 0:
            return False
            break
    return True

angka = int(input("Masukkan angka: "))

if angka_prima(angka):
    print(angka, "adalah angka prima")
else:
    print(angka, "bukan angka prima")