class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
        
    def cetak_informasi(self):
        print("Nama Anda:", self.nama)
        print("Umur Anda:", self.umur, "tahun")
        
nama = input("Masukkan nama Anda:")
umur = input("Masukkan umur Anda:")

# Membuat objek Manusia dan mencetak informasinya
manusia = Manusia(nama, umur)
print("\nInformasi")
manusia.cetak_informasi()
