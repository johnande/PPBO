def derajat_suhu(suhu):
    if suhu < 0 :
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
    
angka = float(input("masukan suhu dalam derajat celcius: "))
derajat = derajat_suhu(angka)
print("Cuaca saat ini:", derajat)