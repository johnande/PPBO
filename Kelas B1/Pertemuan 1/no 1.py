def hitung_mundur(n):
    for i in range(n, -1, -1):
        print(i, end=" ")

try:
    angka = int(input("Masukkan angka: "))
    if angka < 0:
        print("Masukkan angka positif.")
    else:
        hitung_mundur(angka)
except ValueError:
    print("Masukkan harus berupa angka.")
