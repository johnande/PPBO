def hitung_mundur(angka):

  while angka >= 0:
    print(angka, end=" ")
    angka -= 1

# Meminta input angka dari pengguna
angka = int(input("Masukkan angka : "))
  
# Menjalankan fungsi hitung mundur
hitung_mundur(angka)
