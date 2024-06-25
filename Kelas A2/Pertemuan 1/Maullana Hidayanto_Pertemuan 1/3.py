def hitung_nilai_akhir(niu, nilai_tugas, nilai_laporan, nilai_ujian):
  
  # Menghitung rata-rata nilai tugas dan laporan
  rata_rata_tugas_laporan = (nilai_tugas + nilai_laporan) / 2

  # Jika rata-rata kurang dari 40, maka langsung mendapat nilai K
  if rata_rata_tugas_laporan < 40:
    print(f"NIU: {niu}")
    print("Nilai akhir: K")
    return

  # Menghitung nilai akhir
  nilai_akhir = (nilai_tugas * 0.25) + (nilai_laporan * 0.25) + (nilai_ujian * 0.5)

  # Menentukan nilai akhir huruf
  if nilai_akhir >= 80:
    nilai_huruf = "A"
  elif nilai_akhir >= 70:
    nilai_huruf = "B"
  elif nilai_akhir >= 60:
    nilai_huruf = "C"
  elif nilai_akhir >= 50:
    nilai_huruf = "D"
  else:
    nilai_huruf = "E"

  # Menampilkan output nilai akhir huruf
  print(f"NIU: {niu}")
  print(f"Nilai akhir: {nilai_akhir:.2f}")
  print(f"Nilai akhir huruf: {nilai_huruf}")

print("Menghitung Nilai Akhir")
print("======================================")

# Meminta input NIU
niu = int(input("\nMasukkan NIU (6 digit): "))

# Meminta input nilai tugas
nilai_tugas = float(input("Masukkan nilai tugas: "))

# Meminta input nilai laporan
nilai_laporan = float(input("Masukkan nilai laporan: "))

# Meminta input nilai ujian
nilai_ujian = float(input("Masukkan nilai ujian: "))

print("\nNilai Akhir Mahasiswa")
print("======================================")

# Menghitung dan menampilkan nilai akhir
hitung_nilai_akhir(niu, nilai_tugas, nilai_laporan, nilai_ujian)
