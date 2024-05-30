class Buah:
    def __init__(self, nama, harga_per_kg):
        self.nama = nama
        self.harga_per_kg = harga_per_kg
        
    def __mul__(self, berat):
        print('Berat penjualan:', berat, 'kg')
        return self.harga_per_kg * berat
    
class Penjualan_Buah:
    def __init__(self, buah, berat):
        self.buah = buah
        self.berat = berat

# Membuat objek Buah
apel = Buah("Apel", 20000)

# Membuat objek PenjualanBuah
penjualan_apel = Penjualan_Buah(apel, 5)

# Melakukan operasi perkalian menggunakan operator overloading
total_penjualan = apel * penjualan_apel.berat

# Menampilkan total penjualan
print(f'Total penjualan {apel.nama}: {total_penjualan} rupiah')
