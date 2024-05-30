suhu = float(input("Berapa suhu saat ini? "))

if suhu < 0:
    print("Membeku")
elif suhu >= 0 and suhu < 10:
    print("Sangat Dingin")
elif suhu >= 10 and suhu < 20:
    print("Sejuk")
elif suhu >= 20 and suhu < 30:
    print("Hangat")
elif suhu >= 30 and suhu < 40:
    print("Panas")
else:
    print("Sangat Panas")