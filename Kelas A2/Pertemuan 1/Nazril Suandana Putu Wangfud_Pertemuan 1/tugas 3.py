# Mendapatkan input NIU (6 digit integer)
niu = int(input("Masukkan NIU (6 digit integer): "))

# Mendapatkan input nilai tugas
nilai_tugas = float(input("Masukkan nilai tugas: "))

# Mendapatkan input nilai laporan
nilai_laporan = float(input("Masukkan nilai laporan: "))

# Menghitung rata-rata nilai tugas dan laporan
rata_rata = (nilai_tugas + nilai_laporan) / 2

# Memeriksa apakah rata-rata kurang dari 40
if rata_rata < 40:
    nilai_akhir = rata_rata
    keterangan = "K"
else:
    # Mendapatkan input nilai ujian
    nilai_ujian = float(input("Masukkan nilai ujian: "))

    # Menghitung nilai akhir dengan bobot nilai tugas dan laporan masing-masing 25% dan nilai ujian 50%
    nilai_akhir = (0.25 * rata_rata) + (0.5 * nilai_ujian)

    # Menentukan nilai akhir huruf
    if 80 <= nilai_akhir <= 100:
        keterangan = "A"
    elif 70 <= nilai_akhir < 80:
        keterangan = "B"
    elif 60 <= nilai_akhir < 70:
        keterangan = "C"
    elif 50 <= nilai_akhir < 60:
        keterangan = "D"
    else:
        keterangan = "E"

# Menampilkan output nilai akhir dan keterangan
print("NIU:", niu)
print("Nilai akhir:", nilai_akhir)
print("Nilai huruf:", keterangan)