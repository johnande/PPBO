# Meminta input suhu dari pengguna
suhu_celcius = float(input("Masukkan suhu dalam derajat Celcius: "))

# Klasifikasi suhu berdasarkan ketentuan
if suhu_celcius < 0:
    print("Membeku")
elif suhu_celcius < 10:
    print("Sangat Dingin")
elif suhu_celcius < 20:
    print("Sejuk")
elif suhu_celcius < 30:
    print("Hangat")
elif suhu_celcius < 40:
    print("Panas")
else:
    print("Sangat Panas")

