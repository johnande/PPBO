def hitung_nilai_huruf(nilai_akhir):
    if nilai_akhir >= 80:
        return 'A'
    elif nilai_akhir >= 70:
        return 'B'
    elif nilai_akhir >= 60:
        return 'C'
    elif nilai_akhir >= 50:
        return 'D'
    else:
        return 'E'

while True:
    while True:
        niu = input("Masukkan NIU (6 digit integer): ")
        if len(niu) == 6 and niu.isdigit():
            break
        else:
            print("NIU harus berupa 6 digit integer. Silakan coba lagi.")
    
    nilai_tugas = float(input("Masukkan nilai tugas: "))
    nilai_laporan = float(input("Masukkan nilai laporan: "))
    
    rata_rata = (nilai_tugas + nilai_laporan) / 2
    
    if rata_rata < 40:
        print("Rata-rata nilai tugas dan laporan kurang dari 40. Siswa mendapat nilai K.")
    else:
        nilai_ujian = float(input("Masukkan nilai ujian: "))
        
        nilai_akhir = 0.25 * rata_rata + 0.5 * nilai_ujian
        
        nilai_huruf = hitung_nilai_huruf(nilai_akhir)
        print(f"Rata-rata nilai tugas dan laporan: {rata_rata:.2f}")
        print(f"Nilai akhir dengan bobot tugas (25%), laporan (25%), dan ujian (50%): {nilai_akhir:.2f}")
        print(f"Nilai akhir huruf: {nilai_huruf}")
    
    break
