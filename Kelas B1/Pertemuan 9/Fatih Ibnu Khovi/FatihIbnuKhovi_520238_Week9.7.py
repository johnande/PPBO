from collections import namedtuple

Baju = namedtuple('Baju', ['nama', 'harga', 'warna'])

def tampilkan_informasi_baju(baju):
    print("Nama Kaos:", baju.nama)
    print("Harga: Rp.", baju.harga)
    print("Warna:", baju.warna)
    print()

def main():
    baju1 = Baju(nama="Adidas", harga=150000, warna="Merah")
    
    print("Informasi Pakaian:")
    tampilkan_informasi_baju(baju1)
    
if __name__ == "__main__":
    main()