niu = int(input("Masukan NIU: "))
if len(str(niu)) != 6: 
    print("NIU harus terdiri dari 6 digit.")
    exit()

nilai_tugas = int(input("Masukan nilai tugas: "))
nilai_laporan = int(input("Masukan nilai laporan: "))

if (nilai_tugas + nilai_laporan) / 2 < 40:
    print("Siswa mendapat nilai K")
    exit()
else:
    nilai_ujian = int(input("Masukan nilai ujian: "))
    nilai_akhir = (nilai_tugas * 0.25) + (nilai_laporan * 0.25) + (nilai_ujian * 0.5)

    if 80 <= nilai_akhir <= 100:
        nilai_huruf = "A"
    elif 70 <= nilai_akhir < 80:
        nilai_huruf = "B"
    elif 60 <= nilai_akhir < 70:
        nilai_huruf = "C"
    elif 50 <= nilai_akhir < 60:
        nilai_huruf = "D"
    elif nilai_akhir < 50:
        nilai_huruf = "E"
    else:
        nilai_huruf = "Nilai anda diluar nalar"

print("Nilai yang didapatkan siswa dengan NIU", niu , "adalah", nilai_akhir, "(", nilai_huruf, ")")