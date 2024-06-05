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

if __name__ == "__main__":
    try:
        input_suhu = float(input("Masukkan suhu dalam derajat Celcius: "))
        hasil_klasifikasi = klasifikasi_suhu(input_suhu)
        print(f"Klasifikasi suhu: {hasil_klasifikasi}")
    except ValueError:
        print("Masukkan harus berupa nilai numerik.")