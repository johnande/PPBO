def hitung_nilai_akhir(tugas, laporan, ujian):
    rata_rata = (tugas + laporan) / 2
    if rata_rata < 40:
        return 'K'
    else:
        nilai_akhir = 0.25 * rata_rata + 0.5 * ujian
        return nilai_akhir

def nilai_huruf(nilai):
    if nilai >= 80:
        return 'A'
    elif nilai >= 70:
        return 'B'
    elif nilai >= 60:
        return 'C'
    elif nilai >= 50:
        return 'D'
    else:
        return 'E'

try:
    niu = int(input("Masukkan NIU (6 digit integer): "))
    nilai_tugas = float(input("Masukkan nilai tugas: "))
    nilai_laporan = float(input("Masukkan nilai laporan: "))

    rata_rata = (nilai_tugas + nilai_laporan) / 2
    if rata_rata < 40:
        print("Nilai akhir: K")
    else:
        nilai_ujian = float(input("Masukkan nilai ujian: "))
        nilai_akhir = hitung_nilai_akhir(nilai_tugas, nilai_laporan, nilai_ujian)
        nilai_huruf_akhir = nilai_huruf(nilai_akhir)
        print("Nilai akhir:", nilai_akhir)
        print("Nilai huruf:", nilai_huruf_akhir)

except ValueError:
    print("Input yang dimasukkan tidak valid.")

