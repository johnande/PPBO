def main():
    niu = int(input("NIU (6 digit integer): "))
    tugas = float(input("Nilai tugas: "))
    laporan = float(input("Nilai laporan: "))
    
    if (tugas + laporan) / 2 < 40:
        print("Nilai akhir: K")
        return
    
    ujian = float(input("Nilai ujian: "))
    nilai_akhir = (tugas * 0.25) + (laporan * 0.25) + (ujian * 0.5)
    
    if nilai_akhir >= 80:
        print("Nilai akhir: A")
    elif nilai_akhir >= 70:
        print("Nilai akhir: B")
    elif nilai_akhir >= 60:
        print("Nilai akhir: C")
    elif nilai_akhir >= 50:
        print("Nilai akhir: D")
    else:
        print("Nilai akhir: E")

if __name__ == "__main__":
    main()



