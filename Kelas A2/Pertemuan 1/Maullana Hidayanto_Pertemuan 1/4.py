def cek_primer(angka):
    if angka == 1:
        print("Bukan Angka Primer")
    elif angka > 1 :
        for i in range(2, angka):
            if (angka % i) == 0:
                print("Bukan Angka Primer")
                break
        else : print("Angka Primer")

angka = int(input("Masukkan Angka :"))
cek_primer(angka)
