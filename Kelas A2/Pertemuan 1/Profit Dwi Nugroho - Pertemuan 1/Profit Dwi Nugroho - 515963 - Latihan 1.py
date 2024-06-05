def hitung_mundur(angka):
    if angka < 0:
        print("Masukkan angka positif.")
    else:
        for i in range(angka, -1, -1):
            print(i, end=" ")
            
if __name__ == "__main__":
    try:
        input_angka = int(input("Masukkan angka: "))
        hitung_mundur(input_angka)
    except ValueError:
        print("Masukkan harus berupa angka.")