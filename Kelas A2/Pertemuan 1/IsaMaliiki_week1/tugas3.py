import os

while True:
    niu = input("Masukkan NIU Anda: ")
    if len(niu) != 6:
        print("NIU yang Anda masukkan salah")
        pass
    else:
        break

nilai_laporan = float(input("Masukkan Nilai Laporan Anda: "))
nilai_tugas = float(input("Masukkan Nilai Tugas Anda: "))
rata_rata = (nilai_laporan + nilai_tugas) / 2
print(f"Rata-rata nilai awal Anda adalah {rata_rata}")
if rata_rata < 40:
    print("Anda mendapatkan nilai K")
    exit()
else:
    os.system("cls")

print(f"Rata-rata nilai awal Anda adalah {rata_rata}")
nilai_ujian = float(input("Masukkan Nilai Ujian Anda: "))
nilai_akhir = (nilai_laporan + nilai_tugas)*0.25 + nilai_ujian*0.5
print(f"Nilai Anda adalah {nilai_akhir}")
if 80 <= nilai_akhir <= 100:
    print("Nilai Akhir Anda adalah A")
elif 70 <= nilai_akhir < 80:
    print("Nilai Akhir Anda adalah B")
elif 60 <= nilai_akhir < 70:
    print("Nilai Akhir Anda adalah C")
elif 50 <= nilai_akhir < 60:
    print("Nilai Akhir Anda adalah D")
elif nilai_akhir < 50:
    print("Nilai Akhir Anda adalah E")