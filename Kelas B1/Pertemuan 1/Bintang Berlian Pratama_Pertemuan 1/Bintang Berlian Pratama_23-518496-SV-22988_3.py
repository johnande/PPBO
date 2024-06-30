NIU = int(input("Masukkan NIU: "))
tugas = int(input("Masukkan Nilai Tugas: "))
laporan = int(input("Masukkan Nilai Laporan: "))
rata2 = (tugas + laporan) / 2

if rata2 < 40:
    print("K")
else:
    ujian = int(input("Masukkan Nilai Ujian: "))
    nilaiAkhir = (tugas * 0.25) + (laporan * 0.25) + (ujian * 0.5)

    if 80 <= nilaiAkhir <= 100:
        print("A")
    elif 70 <= nilaiAkhir < 80:
        print("B")
    elif 60 <= nilaiAkhir < 70:
        print("C")
    elif 50 <= nilaiAkhir < 60:
        print("D")
    elif nilaiAkhir < 50:
        print("E")
    else:
        print("Nilai tidak terdefinisi")

        
