from abc import ABC, abstractmethod

class MoodTracker(ABC):
    def __init__(self, nama):
        self.nama = nama
    
    @abstractmethod
    def catat_suasana_hati(self, tanggal, suasana_hati):
        pass
    
    @abstractmethod
    def tampilkan_riwayat(self):
        pass

class MoodTrackerBiasa(MoodTracker):
    def __init__(self, nama):
        super().__init__(nama)
        self.riwayat_suasana_hati = {}
    
    def catat_suasana_hati(self, tanggal, suasana_hati):
        self.riwayat_suasana_hati[tanggal] = suasana_hati
    
    def tampilkan_riwayat(self):
        print(f"Riwayat Suasana Hati untuk {self.nama}:")
        for tanggal, suasana_hati in self.riwayat_suasana_hati.items():
            print(f"{tanggal}: {suasana_hati}")

if __name__ == "__main__":
    nama_pengguna = input("Masukkan nama Anda: ")
    mood_tracker = MoodTrackerBiasa(nama_pengguna)
    print(f"Halo {nama_pengguna}! Apa yang ingin Anda lakukan?:")
    
    while True:
        print("\n1. Catat Suasana Hati")
        print("2. Tampilkan Riwayat")
        print("3. Keluar")
        
        pilihan = input("Pilih: ")
        
        if pilihan == "1":
            tanggal = input("Masukkan tanggal (dd/mm/yyyy): ")
            suasana_hati = input("Masukkan suasana hati Anda: ")
            mood_tracker.catat_suasana_hati(tanggal, suasana_hati)
            print("Suasana hati berhasil dicatat.")
        
        elif pilihan == "2":
            mood_tracker.tampilkan_riwayat()
        
        elif pilihan == "3":
            print(f"Terima kasih {nama_pengguna}, jangan lupa bahagia! :))")
            break
        
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")
