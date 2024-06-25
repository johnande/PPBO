from abc import ABC, abstractmethod

class Politisi(ABC):
    def __init__(self, nama, partai, *args, **kwargs):
        self.nama = nama
        self.partai = partai

    @abstractmethod
    def bicara(self):
        pass

class Presiden(Politisi):
    def __init__(self, nama, partai, masa_jabatan, *args, **kwargs):
        super().__init__(nama, partai, *args, **kwargs)
        self.masa_jabatan = masa_jabatan

    def bicara(self):
        print(f"Presiden {self.nama} dari partai {self.partai} sedang memberikan pidato.")

class Menteri(Politisi):
    def __init__(self, nama, partai, pekerjaan, *args, **kwargs):
        super().__init__(nama, partai, *args, **kwargs)
        self.pekerjaan = pekerjaan

    def bicara(self):
        print(f"Menteri {self.nama} dari partai {self.partai} sedang membahas {self.pekerjaan}.")

class Gubernur(Politisi):
    def __init__(self, nama, partai, provinsi, *args, **kwargs):
        super().__init__(nama, partai, *args, **kwargs)
        self.provinsi = provinsi

    def bicara(self):
        print(f"Gubernur {self.nama} dari partai {self.partai} sedang membahas isu di {self.provinsi}.")

# Membuat objek dari kelas Presiden, Menteri, dan Gubernur
presiden = Presiden("Joko Widodo", "PDI-P", "2019-2024")
menteri = Menteri("Sri Mulyani", "Independen", "Keuangan")
gubernur = Gubernur("Ganjar Prakoso", "PDI", "Jawa Tengah")

# Memanggil metode bicara untuk setiap objek
presiden.bicara()
menteri.bicara()
gubernur.bicara()