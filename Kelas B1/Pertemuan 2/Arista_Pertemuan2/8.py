import random

class MakananAnakKos:
    def __init__(self, hari_ini, cuaca, mood):
        self.hari_ini = hari_ini
        self.cuaca = cuaca
        self.mood = mood
    
    def rekomendasi_makanan(self):
        menu_harian = {
            "Senin": {
                "Cerah": ["Nasi Goreng", "Mie Goreng", "Ayam Goreng", "Sayur Asem"],
                "Hujan": ["Bubur Ayam", "Mi Sop", "Rawon", "Bakso"],
                "Lembab": ["Nasi Uduk", "Nasi Liwet", "Lontong Sayur", "Soto Ayam"]
            },
            "Selasa": {
                "Cerah": ["Nasi Kuning", "Ayam Bakar", "Tumis Kangkung", "Pecel Lele"],
                "Hujan": ["Soto Betawi", "Rawon", "Bakso", "Nasi Goreng"],
                "Lembab": ["Sate Kambing", "Soto Ayam", "Ayam Goreng", "Pecel"]
            },
            "Rabu": {
                "Cerah": ["Nasi Padang", "Ayam Goreng", "Rendang", "Sayur Bayam"],
                "Hujan": ["Bubur Ayam", "Rawon", "Mie Ayam", "Nasi Campur"],
                "Lembab": ["Nasi Goreng", "Bakso", "Mie Goreng", "Sop Buntut"]
            },
            "Kamis": {
                "Cerah": ["Nasi Campur", "Ikan Bakar", "Gulai Ayam", "Sayur Asem"],
                "Hujan": ["Nasi Uduk", "Soto Ayam", "Bakso", "Mie Ayam"],
                "Lembab": ["Nasi Goreng", "Mie Goreng", "Bakso", "Rawon"]
            },
            "Jumat": {
                "Cerah": ["Nasi Kebuli", "Ayam Bakar", "Capcay", "Tumis Kangkung"],
                "Hujan": ["Sate Ayam", "Sop Buntut", "Nasi Goreng", "Mie Goreng"],
                "Lembab": ["Nasi Liwet", "Nasi Uduk", "Ayam Goreng", "Bakso"]
            },
            "Sabtu": {
                "Cerah": ["Nasi Pecel", "Oseng-oseng", "Sate Padang", "Sayur Lodeh"],
                "Hujan": ["Bubur Ayam", "Rawon", "Mi Sop", "Mie Goreng"],
                "Lembab": ["Nasi Goreng", "Ayam Goreng", "Mie Goreng", "Capcay"]
            },
            "Minggu": {
                "Cerah": ["Nasi Liwet", "Sop Iga", "Ayam Bakar", "Sayur Asam"],
                "Hujan": ["Sop Buntut", "Bakso", "Nasi Goreng", "Mie Goreng"],
                "Lembab": ["Nasi Uduk", "Ayam Goreng", "Bakso", "Mie Ayam"]
            }
        }
        
        if self.hari_ini in menu_harian:
            menu_cuaca = menu_harian[self.hari_ini].get(self.cuaca)
            if menu_cuaca:
                return random.choice(menu_cuaca)
            else:
                return f"Tidak ada rekomendasi untuk cuaca {self.cuaca}"
        else:
            return "Hari ini tidak ada rekomendasi menu, silakan coba lagi besok!"

# Penggunaan program
hari_ini = input("Masukkan hari ini: ")
cuaca = input("Masukkan kondisi cuaca (Cerah/Hujan/Lembab): ")
mood = input("Masukkan mood kamu (Senang/Stres/Lelah): ")

makanan_anak_kos = MakananAnakKos(hari_ini, cuaca, mood)
rekomendasi = makanan_anak_kos.rekomendasi_makanan()

print(f"Rekomendasi makanan untuk hari ini ({hari_ini}), kondisi cuaca ({cuaca}), dan mood Anda ({mood}): {rekomendasi}")
