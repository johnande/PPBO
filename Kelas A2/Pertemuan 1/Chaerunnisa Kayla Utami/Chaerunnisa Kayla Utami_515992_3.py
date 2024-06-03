def nilai_akhir_siswa(niu, nilai_tugas, nilai_laporan, nilai_ujian):
  """
  Fungsi untuk menghitung nilai akhir siswa berdasarkan nilai tugas, laporan, dan ujian

  Args:
    niu: Nomor Induk Siswa (integer)
    nilai_tugas: Nilai tugas (float)
    nilai_laporan: Nilai laporan (float)
    nilai_ujian: Nilai ujian (float)

  Returns:
    Tuple yang berisi:
      * Nilai akhir angka (float)
      * Nilai akhir huruf (string)
  """

# Hitung rata-rata nilai tugas dan laporan
  rata_rata_tugas_laporan = (nilai_tugas + nilai_laporan) / 2

# Periksa apakah memenuhi syarat nilai minimum
  if rata_rata_tugas_laporan < 40:
    return 0, "K"  # Nilai K jika rata-rata kurang dari 40

# Hitung nilai akhir dengan bobot
  nilai_akhir_angka = (nilai_tugas * 0.25) + (nilai_laporan * 0.25) + (nilai_ujian * 0.5)

# Tentukan nilai akhir huruf berdasarkan nilai angka
  nilai_akhir_huruf = None
  if nilai_akhir_angka >= 80:
    nilai_akhir_huruf = "A"
  elif nilai_akhir_angka >= 70:
    nilai_akhir_huruf = "B"
  elif nilai_akhir_angka >= 60:
    nilai_akhir_huruf = "C"
  elif nilai_akhir_angka >= 50:
    nilai_akhir_huruf = "D"
  else:
    nilai_akhir_huruf = "E"

  return nilai_akhir_angka, nilai_akhir_huruf

# Input data siswa
niu = int(input("Masukkan NIU: "))
nilai_tugas = float(input("Masukkan nilai tugas: "))
nilai_laporan = float(input("Masukkan nilai laporan: "))
nilai_ujian = float(input("Masukkan nilai ujian: "))

# Hitung dan tampilkan nilai akhir
nilai_akhir_angka, nilai_akhir_huruf = nilai_akhir_siswa(niu, nilai_tugas, nilai_laporan, nilai_ujian)

print(f"NIU: {niu}")
print(f"Nilai Akhir Angka: {nilai_akhir_angka:.2f}")
print(f"Nilai Akhir Huruf: {nilai_akhir_huruf}")
