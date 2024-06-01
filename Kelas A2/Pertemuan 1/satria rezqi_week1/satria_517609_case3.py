import numpy as np

def final_result (NIU:int, exam:float, report:float) -> str:

    avg = np.average([exam, report])

    if avg < 40:
        return f"rata-rata {avg}, maka mendapat nilai: K"
    
    else:
        nilai_ujian = float(input("masukkan nilai ujian\t: "))
        nilai_akhir = exam*0.25 + report*0.25 + nilai_ujian*0.5
        print()

        if nilai_akhir >= 80 and nilai_akhir <= 100:
            return f'rata-rata = {nilai_akhir}, maka mendapat nilai: A'
        
        elif nilai_akhir >= 70 and nilai_akhir < 80:
            return f"rata-rata = {nilai_akhir}, maka mendapat nilai: B"
        
        elif nilai_akhir >= 60 and nilai_akhir < 70:
            return f"rata-rata = {nilai_akhir}, maka mendapat nilai: C"
        
        elif nilai_akhir >= 50 and nilai_akhir < 60:
            return f"rata-rata = {nilai_akhir}, maka mendapat nilai: D"
        
        else:
            return f"rata-rata = {nilai_akhir}, maka mendapat nilai: E"



niu = input("masukkan NIU\t: ")

while len (niu) != 6:
    niu = input("masukkan NIU\t: ")

niu = int(niu)

nilai_tugas = float(input("masukkan nilai tugas\t: "))
nilai_laporan = float(input("masukkan nilai laporan\t: "))

print(final_result(niu, nilai_tugas, nilai_laporan))