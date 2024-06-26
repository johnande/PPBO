while True:
    jumlah_mil = input("Jumlah mil yang ingin Anda konversi ke kilometer: ")
    if jumlah_mil.replace('.', '', 1).isdigit(): 
        mil = float(jumlah_mil)
        km = mil * 1.60934
        print(f"{mil} mil = {km:.3f} kilometer")
        break
    else:
        print("Angka yang Anda masukkan tidak valid. Silakan coba lagi!")
