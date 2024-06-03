# Program menentukan nilai siswa

# Meminta input NIU
niu = int(input("Masukkan NIU (6 digit integer): "))

# Meminta input nilai tugas
nilai_tugas = float(input("Masukkan nilai tugas: "))

# Meminta input nilai laporan
nilai_laporan = float(input("Masukkan nilai laporan: "))

# Menghitung rata-rata nilai tugas dan laporan
rata_rata = (nilai_tugas + nilai_laporan) / 2

# Memeriksa jika rata-rata kurang dari 40, maka beri nilai K dan program berakhir
if rata_rata < 40:
    print("Nilai akhir: K")
else:
    # Meminta input nilai ujian
    nilai_ujian = float(input("Masukkan nilai ujian: "))

    # Menghitung nilai akhir dengan bobot
    nilai_akhir = 0.25 * rata_rata + 0.5 * nilai_ujian

    # Menentukan nilai huruf berdasarkan nilai akhir
    if 80 <= nilai_akhir <= 100:
        nilai_huruf = 'A'
    elif 70 <= nilai_akhir < 80:
        nilai_huruf = 'B'
    elif 60 <= nilai_akhir < 70:
        nilai_huruf = 'C'
    elif 50 <= nilai_akhir < 60:
        nilai_huruf = 'D'
    else:
        nilai_huruf = 'E'

    # Menampilkan output nilai akhir huruf
    print(f"Nilai akhir: {nilai_akhir:.2f} - Nilai huruf: {nilai_huruf}")

