def mil_ke_km():
    mil = float(input("Masukkan nilai mil untuk dikonversi ke kilometer: "))
    km = mil*1.609
    print(f"{mil} mil = {km} kilometer")
    return km

kilometer = mil_ke_km()