def klasifikasi_suhu(suhu):
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
    else:
        print("Sangat Panas")

try:
    suhu = float(input("Masukkan suhu dalam derajat Celcius: "))
    klasifikasi_suhu(suhu)
except ValueError:
    print("Input yang dimasukkan bukan angka.")

