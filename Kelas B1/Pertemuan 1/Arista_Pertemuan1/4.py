angka = int(input("Masukkan angka: "))

if angka > 1:
    for i in range(2, angka):
        if (angka % i) == 0:
            print("bukan angka prima")
            break
    else:
        print("angka prima")
else:
    print("bukan angka prima")
