def klasifikasi_suhu(suhu):
    if suhu < 0:
        return "Membeku"
    elif 0 <= suhu < 10:
        return "Sangat Dingin"
    elif 10 <= suhu < 20:
        return "Sejuk"
    elif 20 <= suhu < 30:
        return "Hangat"
    elif 30 <= suhu < 40:
        return "Panas"
    else:
        return "Sangat Panas"

suhu = float(input("Masukkan suhu: "))
klasifikasi = klasifikasi_suhu(suhu)
print("Klasifikasi suhu:", klasifikasi)