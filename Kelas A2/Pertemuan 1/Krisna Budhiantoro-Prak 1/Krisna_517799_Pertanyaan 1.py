suhu = float(input("Masukkan nilai suhu (Celsius): "))

if suhu < 0:
    klasifikasi = "Membeku"
elif suhu < 10:
    klasifikasi = "Sangat Dingin"
elif suhu < 20:
    klasifikasi = "Sejuk"
elif suhu < 30:
    klasifikasi = "Hangat"
elif suhu < 40:
    klasifikasi = "Panas"
else:
    klasifikasi = "Sangat Panas"

print(f"Suhu {suhu} derajat Celsius diklasifikasikan sebagai {klasifikasi}")
