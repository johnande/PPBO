# Minta input NIU
niu = int(input("Masukkan NIU (6 digit integer): "))

# Minta nilai tugas
nilai_tugas = float(input("Masukkan nilai tugas: "))

# Minta nilai laporan
nilai_laporan = float(input("Masukkan nilai laporan: "))

# Hitung rata-rata nilai tugas dan laporan
rata_rata = (nilai_tugas + nilai_laporan) / 2

# Cek jika rata-rata kurang dari 40, berikan nilai K dan program selesai
if rata_rata < 40:
    print("Nilai akhir: K")
else:
    # Minta nilai ujian
    nilai_ujian = float(input("Masukkan nilai ujian: "))

    # Hitung nilai akhir
    nilai_akhir = 0.25 * rata_rata + 0.5 * nilai_ujian

    # Tentukan nilai huruf berdasarkan nilai akhir
    if 80 <= nilai_akhir <= 100:
        nilai_huruf = "A"
    elif 70 <= nilai_akhir < 80:
        nilai_huruf = "B"
    elif 60 <= nilai_akhir < 70:
        nilai_huruf = "C"
    elif 50 <= nilai_akhir < 60:
        nilai_huruf = "D"
    else:
        nilai_huruf = "E"

    # Tampilkan output nilai akhir huruf
    print(f"Nilai akhir: {nilai_huruf}")
