NIU = int(input("Masukkan NIU (6 digit integer): "))
nilai_tugas = float(input("Masukkan nilai tugas: "))
nilai_laporan = float(input("Masukkan nilai laporan: "))

# Program menghitung rata-rata nilai tugas dan laporan
rata_rata = (nilai_tugas + nilai_laporan) / 2

# Jika rata-rata kurang dari 40, maka output program “K” dan program berakhir
if rata_rata < 40:
    print("K")
else:
    # Program meminta input ujian
    nilai_ujian = float(input("Masukkan nilai ujian: "))

    # Program menghitung nilai akhir dengan bobot nilai tugas dan laporan masing-masing 25% dan nilai ujian 50%
    nilai_akhir = (nilai_tugas * 0.25) + (nilai_laporan * 0.25) + (nilai_ujian * 0.5)

    # Program menampilkan output nilai akhir huruf berdasarkan nilai akhir angka
    if 80 <= nilai_akhir <= 100:
        print("A")
    elif 70 <= nilai_akhir < 80:
        print("B")
    elif 60 <= nilai_akhir < 70:
        print("C")
    elif 50 <= nilai_akhir < 60:
        print("D")
    elif 40 <= nilai_akhir < 60:
        print("D")
    else:
        print("E")