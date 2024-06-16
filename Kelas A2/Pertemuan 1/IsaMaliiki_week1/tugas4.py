angka = int(input("Masukkan Angka: "))
hasil = "angka primer"
bukan_prima = "bukan angka primer"

if angka <= 1:
    hasil = bukan_prima
    exit()
for i in range (2, angka):
    if angka % i == 0:
        hasil = bukan_prima
        break

print(hasil)