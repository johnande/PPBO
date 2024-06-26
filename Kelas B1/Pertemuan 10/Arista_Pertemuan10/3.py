from abc import ABC, abstractmethod

class AngkutanKota(ABC):
    @abstractmethod
    def pesan_tiket(self, destinasi: str, jumlah_penumpang: int):
        pass

class Bus(AngkutanKota):
    def pesan_tiket(self, destinasi: str, jumlah_penumpang: int):
        return f"Memesan tiket bus untuk destinasi {destinasi} untuk {jumlah_penumpang} penumpang"

class Angkot(AngkutanKota):
    def pesan_tiket(self, destinasi: str, jumlah_penumpang: int):
        return f"Memesan tiket angkot untuk rute {destinasi} untuk {jumlah_penumpang} penumpang"

class Travel(AngkutanKota):
    def pesan_tiket(self, destinasi: str, jumlah_penumpang: int):
        return f"Memesan tiket travel untuk tujuan {destinasi} untuk {jumlah_penumpang} penumpang"

class AngkutanKotaFactory:
    def create_angkutan_kota(self, jenis_angkutan: str):
        if jenis_angkutan.lower() == "bus":
            return Bus()
        elif jenis_angkutan.lower() == "angkot":
            return Angkot()
        elif jenis_angkutan.lower() == "travel":
            return Travel()
        else:
            return None

def main():
    factory = AngkutanKotaFactory()
    jenis_angkutan = input("Selamat datang di layanan pemesanan tiket angkutan kota. Silakan pilih jenis angkutan (bus/angkot/travel): ")
    angkutan = factory.create_angkutan_kota(jenis_angkutan)
    if angkutan:
        destinasi = input("Masukkan destinasi Anda: ")
        jumlah_penumpang = int(input("Masukkan jumlah penumpang: "))
        print(angkutan.pesan_tiket(destinasi, jumlah_penumpang))
    else:
        print("Jenis angkutan yang dimasukkan tidak valid.")

if __name__ == "__main__":
    main()
