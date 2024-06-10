def hitung_mundur(angka):
    for i in range(angka, -1, -1):
        print(i, end=' ')

try:
    angka = int(input("Masukkan angka: "))
    hitung_mundur(angka)
except ValueError:
    print("Input yang dimasukkan bukan angka.")

