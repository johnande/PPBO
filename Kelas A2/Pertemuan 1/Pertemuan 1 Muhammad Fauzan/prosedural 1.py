def hitung_mundur_horizontal(angka):
    if not angka.isdigit():
        print("Masukkan harus berupa angka.")
        return

    angka = int(angka)

    print("Hitung mundur:")
    for i in range(angka, -1, -1):
        print(i, end=" ")

masukkan_angka = input("Input angka: ")
hitung_mundur_horizontal(masukkan_angka)

