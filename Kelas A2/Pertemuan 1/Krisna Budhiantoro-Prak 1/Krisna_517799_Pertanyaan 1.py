def hitung_mundur(angka):
    for i in range(angka, -1, -1):
        print(i, end=' ')

angka_input = int(input("Masukkan angka: "))

hitung_mundur(angka_input)
