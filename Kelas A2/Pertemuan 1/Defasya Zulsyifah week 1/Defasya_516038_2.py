# Menerima input suhu dari pengguna
suhu = float(input("Masukkan suhu dalam derajat Celcius: "))

# Klasifikasi suhu dan mencetak output yang sesuai
if suhu < 0:
    hasil = "Membeku"
elif suhu < 10:
    hasil = "Sangat Dingin"
elif suhu < 20:
    hasil = "Sejuk"
elif suhu < 30:
    hasil = "Hangat"
elif suhu < 40:
    hasil = "Panas"
else:
    hasil = "Sangat Panas"

print(hasil)

