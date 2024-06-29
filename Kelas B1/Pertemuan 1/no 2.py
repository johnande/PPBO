def klasifikasi_suhu(suhu):
    if suhu < 0:
        return "Membeku"
    elif suhu < 10:
        return "Sangat Dingin"
    elif suhu < 20:
        return "Sejuk"
    elif suhu < 30:
        return "Hangat"
    elif suhu < 40:
        return "Panas"
    else:
        return "Sangat Panas"

try:
    suhu_celcius = float(input("Masukkan suhu dalam derajat Celcius: "))
    klasifikasi = klasifikasi_suhu(suhu_celcius)
    print("Klasifikasi suhu:", klasifikasi)
except ValueError:
    print("Masukkan harus berupa angka.")
