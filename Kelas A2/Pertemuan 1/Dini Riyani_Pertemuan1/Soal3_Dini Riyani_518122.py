def niu():
    niu = int(input("Masukkan NIU: "))
    while len(str(niu)) != 6:
        print("NIU harus berisi 6 angka!!!")
        niu = int(input("Masukkan NIU: "))
        return (niu)

def nilai():
    nilai_tugas = int(input("Masukkan Nilai Tugas: "))
    nilai_laporan = int(input("Masukkan Nilai Laporan: "))
    rata_rata_nilai = (nilai_tugas + nilai_laporan) / 2
    if rata_rata_nilai < 40:
        print("Nilai anda 'K'")
    else:
      nilai_ujian = int(input("Masukkan Nilai Ujian: "))
      nilai_akhir = (nilai_tugas * 0.25) + (nilai_laporan * 0.25) + (nilai_ujian * 0.5)
      if nilai_akhir >= 80:
        print("A")
      elif nilai_akhir >= 70:
        print("B")
      elif nilai_akhir >= 60:
        print("C")
      elif nilai_akhir >= 50:
        print("D")
      else:
        print("E")

def main() :
  niu()
  nilai()

if __name__ == "__main__":
    main()
