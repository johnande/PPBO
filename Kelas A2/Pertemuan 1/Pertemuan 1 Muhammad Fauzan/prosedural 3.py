import os

while True :
    niu = input("Masukkan NIU milik anda: ")
    if not niu.isdigit() or len(niu) != 6:
        print("NIU yang anda masukkan salah.")
        pass
    else:
        break

nilai_tugas = float(input("Masukkan nilai tugas: "))
nilai_laporan = float(input("Masukkan nilai laporan: "))
rata_rata = (nilai_tugas + nilai_laporan) / 2
print(f"rata-rata nilai awal anda adalah {rata_rata}")
if rata_rata < 40:
    print("Nilai anda yaitu K")
    exit()
else:
    os.system("cls")

print(f"rata-rata nilai awal anda adalah {rata_rata}")
nilai_ujian = float(input("Masukkan nilai ujian milik anda: "))
nilai_akhir = (nilai_laporan + nilai_tugas)*0.25 + nilai_ujian*0.5
if 80 <= nilai_akhir <= 100:
    nilai_huruf = 'nilai akhir anda dapat A'
elif 70 <= nilai_akhir < 80:
    nilai_huruf = 'nilai akhir anda dapat B'
elif 60 <= nilai_akhir < 70:
    nilai_huruf = 'nilai akhir anda dapat C'
elif 50 <= nilai_akhir < 60:
    nilai_huruf = 'nilai akhir anda dapat D'
else:
    nilai_huruf = 'nilai akhir anda dapat E'

print(f"Nilai akhir huruf: {nilai_huruf}")
