class Orang:
    def __init__(self, nama_depan, nama_belakang, nomer_ID):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomer_ID = nomer_ID

orang1 = Orang("John", "Doe", "123456")
orang2 = Orang("Jane", "Doe", "789012")

print("Orang 1:")
print("Nama Depan:", orang1.nama_depan)
print("Nama Belakang:", orang1.nama_belakang)
print("Nomor ID:", orang1.nomer_ID)

print("\nOrang 2:")
print("Nama Depan:", orang2.nama_depan)
print("Nama Belakang:", orang2.nama_belakang)
print("Nomor ID:", orang2.nomer_ID)
