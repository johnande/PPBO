# Minta input angka dari pengguna
angka = int(input("Masukkan angka: "))

# Cek jika angka kurang dari 2
if angka < 2:
    print("Bukan angka prima")
else:
    # Loop untuk memeriksa apakah angka prima atau bukan
    for i in range(2, int(angka**0.5) + 1):
        if angka % i == 0:
            print("Bukan angka prima")
            break
    else:
        print("Angka prima")
