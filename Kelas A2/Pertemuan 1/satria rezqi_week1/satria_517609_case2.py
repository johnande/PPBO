def temperature (celcius:float) -> str:

    if float(celcius) <= 0 :
        return "membeku"
    
    elif float(celcius) > 0 and float(celcius) <= 10:
        return "sangat dingin"
    
    elif float(celcius) > 10 and float(celcius) <= 20:
        return "sejuk"
    
    elif float(celcius) > 20 and float(celcius) <= 30:
        return "hangat"
    
    elif float(celcius) > 30 and float(celcius) < 40:
        return "panas"
    
    else:
        return "sangat panas"
    
tempt = input ("masukkan suhu: ")

print(temperature(tempt))


