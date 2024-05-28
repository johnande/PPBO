# Minta input angka dari pengguna
angka = int(input("Masukkan angka: "))

# Cek apakah angka positif
if angka < 0:
    print("Masukkan angka positif.")
else:
    # Hitung mundur dan cetak output
    for i in range(angka, -1, -1):
        print(i, end=" ")
