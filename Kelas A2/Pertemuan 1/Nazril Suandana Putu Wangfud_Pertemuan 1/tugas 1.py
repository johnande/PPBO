# Mendapatkan input angka dari pengguna
angka = int(input("Masukkan angka: "))

# Melakukan hitung mundur dari angka yang diinput
for i in range(angka, -1, -1):
    print(i, end=" ")

# Menampilkan nilai 0 pada baris baru
print()

