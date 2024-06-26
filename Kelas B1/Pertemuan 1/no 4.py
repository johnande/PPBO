def cek_bilangan_prima(angka):
    if angka <= 1:
        return False
    elif angka <= 3:
        return True
    elif angka % 2 == 0 or angka % 3 == 0:
        return False
    i = 5
    while i * i <= angka:
        if angka % i == 0 or angka % (i + 2) == 0:
            return False
        i += 6
    return True

try:
    angka = int(input("Masukkan angka: "))
    if cek_bilangan_prima(angka):
        print("Angka prima")
    else:
        print("Bukan angka prima")
except ValueError:
    print("Masukkan harus berupa angka.")
