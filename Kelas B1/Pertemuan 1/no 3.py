def hitung_nilai_akhir(tugas, laporan, ujian):
    rata_rata = (tugas + laporan) / 2
    if rata_rata < 40:
        return "K"
    else:
        nilai_akhir = (tugas * 0.25) + (laporan * 0.25) + (ujian * 0.5)
        return nilai_akhir

def konversi_nilai_huruf(nilai_akhir):
    if nilai_akhir >= 80:
        return "A"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 60:
        return "C"
    elif nilai_akhir >= 50:
        return "D"
    else:
        return "E"

try:
    niu = int(input("Masukkan NIU (6 digit integer): "))
    tugas = float(input("Masukkan nilai tugas: "))
    laporan = float(input("Masukkan nilai laporan: "))
    
    rata_rata = (tugas + laporan) / 2
    if rata_rata < 40:
        print("Nilai akhir: K")
    else:
        ujian = float(input("Masukkan nilai ujian: "))
        nilai_akhir = hitung_nilai_akhir(tugas, laporan, ujian)
        nilai_huruf = konversi_nilai_huruf(nilai_akhir)
        print("Nilai akhir: {}".format(nilai_huruf))
except ValueError:
    print("Masukkan harus sesuai dengan format yang diminta.")
