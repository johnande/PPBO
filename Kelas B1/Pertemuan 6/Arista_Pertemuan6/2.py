from abc import ABC, abstractmethod

class Wisata(ABC):
    def __init__(self, nama, harga_tiket):
        self.nama = nama
        self.harga_tiket = harga_tiket
    
    @abstractmethod
    def deskripsi(self):
        pass

    @abstractmethod
    def hitung_biaya(self, jumlah_mahasiswa):
        pass

    @abstractmethod
    def ulti(self):
        pass

class Pantai(Wisata):
    def deskripsi(self):
        return f"{self.nama} adalah objek wisata pantai dengan harga tiket {self.harga_tiket} per orang."

    def hitung_biaya(self, jumlah_mahasiswa):
        total_biaya = self.harga_tiket * jumlah_mahasiswa
        return f"Biaya total untuk {jumlah_mahasiswa} mahasiswa adalah {total_biaya}."

    def ulti(self):
        return f"Anda bisa menikmati sunset yang indah di sini."

class GarudaWisnuKencana(Wisata):
    def deskripsi(self):
        return f"{self.nama} adalah objek wisata dengan harga tiket {self.harga_tiket} per orang."

    def hitung_biaya(self, jumlah_mahasiswa):
        total_biaya = self.harga_tiket * jumlah_mahasiswa
        return f"Biaya total untuk {jumlah_mahasiswa} mahasiswa adalah {total_biaya}."

    def ulti(self):
        return f"Anda dapat menikmati pemandangan patung Garuda Wisnu Kencana yang megah di sini."

pantai_pandawa = Pantai("Pantai Pandawa", 8000)
garuda_wisnu_kencana = GarudaWisnuKencana("Taman Garuda Wisnu Kencana", 85000)

print(pantai_pandawa.deskripsi())
print(pantai_pandawa.hitung_biaya(30))
print(pantai_pandawa.ulti())
print()

print(garuda_wisnu_kencana.deskripsi())
print(garuda_wisnu_kencana.hitung_biaya(40))
print(garuda_wisnu_kencana.ulti())
