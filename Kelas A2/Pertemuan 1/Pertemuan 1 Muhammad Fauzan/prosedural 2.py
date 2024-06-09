def hitung_suhu(suhu):
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

input_suhu = input("Masukkan suhu dalam bentuk derajat Celcius: ")

try:
    suhu = float(input_suhu)
    hasil_klasifikasi = hitung_suhu(suhu)
    print(f"hasil suhu merupakan: {hasil_klasifikasi}")
except ValueError:
    print("Masukkan harus berupa angka.")
