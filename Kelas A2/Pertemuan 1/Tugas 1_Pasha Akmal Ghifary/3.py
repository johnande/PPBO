niu = int(input("Masukkan NIU (6 digit): "))

nilai_tugas = float(input("Masukkan nilai tugas: "))

nilai_laporan = float(input("Masukkan nilai laporan: "))

rata_rata = (nilai_tugas + nilai_laporan) / 2

if rata_rata < 40:
    print("Siswa mendapat nilai K karena rata-rata nilai kurang dari 40.")
else:

    nilai_ujian = float(input("Masukkan nilai ujian: "))
        
    nilai_akhir = (nilai_tugas * 0.25) + (nilai_laporan * 0.25) + (nilai_ujian * 0.5)

    
    if 80 <= nilai_akhir <= 100:
        print("Hasil: A")
    elif 70 <= nilai_akhir < 80:
        print("Hasil: B")
    elif 60 <= nilai_akhir < 70:
        print("Hasil: C")
    elif 50 <= nilai_akhir < 60:
        print("Hasil: D")
    else:
        print("Hasil: E")
