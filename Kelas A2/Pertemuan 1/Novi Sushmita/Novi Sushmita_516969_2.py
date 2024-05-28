print("Program Mengecek Suhu")
suhu = float(input("Masukkan suhu ruangan (\u00b0C): "))

if suhu < 0:
    print("Membeku")
elif suhu < 10:
    print("Sangat Dingin")
elif suhu < 20:
    print("Sejuk")
elif suhu < 30:
    print("Hangat")
elif suhu < 40:
    print("Panas")
elif suhu >= 40:
    print("Sangat Panas")
