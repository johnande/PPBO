print("Program Mengecek Angka Primer")
angka = int(input("Masukkan sebuah angka: "))

if angka > 1:
    for i in range(2, angka):
        if angka % i == 0:
            print("Bukan angka primer")
            break
    else:
        print("Angka primer")
else:
    print("Bukan angka primer")