def hitung_mundur(angka):
  """
  Fungsi untuk menghitung mundur dari angka yang diberikan

  Args:
    angka: Angka awal untuk hitung mundur

  Returns:
    None. Mencetak hasil hitung mundur ke konsol
  """
  for i in range(angka, -1, -1):
    print((i), end=" ")

# Masukkan angka awal
angka = int(input("Masukkan angka awal: "))

# Jalankan fungsi hitung mundur
hitung_mundur(angka)
