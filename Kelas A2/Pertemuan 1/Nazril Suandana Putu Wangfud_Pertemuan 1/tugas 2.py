# Mendapatkan input suhu dalam derajat Celcius
suhu = float(input("Masukkan nilai suhu dalam derajat Celcius: "))

# Mengklasifikasikan suhu
if suhu < 0:
    kelas_suhu = "Membeku"
elif suhu < 10:
    kelas_suhu = "Sangat Dingin"
elif suhu < 20:
    kelas_suhu = "Sejuk"
elif suhu < 30:
    kelas_suhu = "Hangat"
elif suhu < 40:
    kelas_suhu = "Panas"
else:
    kelas_suhu = "Sangat Panas"

# Menampilkan hasil klasifikasi suhu
print("Klasifikasi suhu:", kelas_suhu)