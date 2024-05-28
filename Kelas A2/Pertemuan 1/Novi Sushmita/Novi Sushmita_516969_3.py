print("Program Menghitung Nilai")
niu_siswa = int(input("Masukkan NIU mahasiswa (6 digit integer): "))
while len(str(niu_siswa)) != 6:
    print("NIU harus berupa 6 digit integer.")
    niu_siswa = input("Masukkan NIU Mahasiswa (6 digit integer): ")

nilai_tugas = float(input("Masukkan nilai tugas: "))
nilai_laporan = float(input("Masukkan nilai laporan: "))
rata_rata = (nilai_tugas + nilai_laporan)/2

if rata_rata < 40:
    print(f"Nilai: K (Rata-rata nilai tugas dan laporan di bawah 40.0: {rata_rata})")
else:
    nilai_ujian = float(input("Masukkan nilai ujian: "))
    bobot_tugas = nilai_tugas/25
    bobot_laporan = nilai_laporan/25
    bobot_ujian = nilai_ujian/50
    total_nilai = (bobot_tugas + bobot_laporan + bobot_ujian) * 10
    if 80 <= total_nilai <=100:
        print(f"Nilai: A (Nilai akhir 80-100: {total_nilai})")
    elif 70 <= total_nilai < 80:
        print(f"Nilai: B (Nilai akhir 70-79: {total_nilai})")
    elif 60 <= total_nilai < 70:
        print(f"Nilai: C (Nilai akhir 60-69: {total_nilai})")
    elif 50 <= total_nilai < 60:
        print(f"Nilai: D (Nilai akhir 50-59: {total_nilai})")
    elif total_nilai < 50:
        print(f"Nilai: E (Nilai akhir di bawah 50: {total_nilai})")