# Mendapatkan input angka
angka = int(input("Masukkan angka: "))

# Memeriksa apakah angka lebih besar dari 1
if angka > 1:
    # Memeriksa apakah angka prima
    prima = True
    for i in range(2, angka):
        if angka % i == 0:
            prima = False
            break

    # Menampilkan hasil cek
    if prima:
        print(angka, "adalah angka prima")
    else:
        print(angka, "bukan angka prima")
else:
    print(angka, "bukan angka prima")