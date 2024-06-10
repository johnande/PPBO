from abc import ABC, abstractmethod

class Barang(ABC):
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
    
    @abstractmethod
    def tampil_info(self):
        pass

class Hijab(Barang):
    def tampil_info(self):
        print(f"Hijab: {self.nama}, Harga: {self.harga}")

class KeranjangBelanja:
    def __init__(self):
        self.barang = []
    
    def tambah_barang(self, barang):
        self.barang.append(barang)
    
    def tampilkan_barang(self):
        total_harga = sum(barang.harga for barang in self.barang)
        print("\nDaftar Barang Belanjaan:")
        print("-------------------------")
        for barang in self.barang:
            barang.tampil_info()
            print("-------------------------")
        print(f"Total harga belanjaan: {total_harga}")

# Fungsi untuk menambahkan jilbab ke keranjang belanja
def tambah_jilbab_ke_keranjang():
    print("Pilih hijab yang ingin ditambahkan:")
    print("1. Bergo - Harga: Rp 18.000")
    print("2. Segi Empat - Harga: Rp 25.000")
    print("3. Pashmina - Harga: Rp 32.000")
    print("Ketik 's' untuk selesai.")
    print("-------------------------")

    while True:
        pilihan = input("Masukkan nomor atau 's': ")
        
        if pilihan.lower() == "s":
            break
        elif pilihan == "1":
            hijab = Hijab("Bergo", 18000)
        elif pilihan == "2":
            hijab = Hijab("Segi Empat", 25000)
        elif pilihan == "3":
            hijab = Hijab("Pashmina", 32000)
        else:
            print("Nomor tidak valid. Silakan coba lagi.")
            continue
        
        keranjang.tambah_barang(hijab)

# Membuat objek keranjang belanja
keranjang = KeranjangBelanja()

# Menambahkan jilbab ke keranjang belanja
tambah_jilbab_ke_keranjang()

# Menampilkan jilbab yang ada di keranjang belanja
keranjang.tampilkan_barang()
