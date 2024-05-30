from collections import namedtuple

Kendaraan = namedtuple("Kendaraan", ["jenis", "plat_nomor", "durasi"])

@staticmethod
def hitung_biaya_parkir(self):
    print("Nama :", self.jenis)
    print("Plat Nomor : ", self.plat_nomor)
    print("Biaya : ", self.durasi * 2000)

Kendaraan.hitung_biaya_parkir = hitung_biaya_parkir

kendaraan1 = Kendaraan("Vario Merah", "AD 2020 JB", 2)
Kendaraan.hitung_biaya_parkir(kendaraan1)