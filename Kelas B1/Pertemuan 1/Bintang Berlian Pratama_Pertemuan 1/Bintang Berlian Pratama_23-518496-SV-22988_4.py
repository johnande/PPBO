angka = int(input("Masukkan angka: "))

if angka > 1:
    prima = True
    for i in range(2, angka):
        if angka % i == 0:
            prima = False
            break
    if prima:
        print("Angka Prima")
    else:
        print("Bukan Angka Prima")
else:
    print("Bukan Angka Prima")  

    