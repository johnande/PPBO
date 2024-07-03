class karyawan:
    gaji_bulanan = 2500000
    def __init__(self, nomor, nama, denda):
        self.nomor = nomor
        self.nama = nama
        self.denda = denda

    @classmethod
    def gaji_sisa(cls, denda):
        return cls.gaji_bulanan - denda

    @staticmethod
    def hitung_sisa(denda):
        return karyawan.gaji_bulanan - denda

    @property
    def data(self):
        return f"{self.nomor}, {self.nama}, {self.denda}"
    
kryw = karyawan("ID0003", "Bagus Putra", 75000)

#Memanggil classmethod
print("Gaji - denda :",karyawan.gaji_sisa(125000))
#Memanggil @staticmethod
print("Gaji yang didapat:",kryw.hitung_sisa(75000))
#Memanggil @property (tanpa tanda kurung)
print(kryw.data)