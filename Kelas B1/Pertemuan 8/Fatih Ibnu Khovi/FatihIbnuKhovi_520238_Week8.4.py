class Rekening:
    def __init__(self, nama, no_rekening, saldo):
        self.nama = nama
        self.no_rekening = no_rekening
        self.saldo = saldo

class Nasabah(Rekening):
    def __init__(self, nama, no_rekening, saldo):
        super().__init__(nama, no_rekening, saldo)

Nasabah1 = Nasabah("Budi", int(5555), float(500000))
Nasabah2 = Nasabah("Wati", int(6666), float(2000000))

print("Informasi Nasabah 1:")
print("Nama:", Nasabah1.nama)
print("Nomor Rekening:", Nasabah1.no_rekening)
print("Saldo:", Nasabah1.saldo)

print(" ")

print("Informasi Nasabah 2:")
print("Nama:", Nasabah2.nama)
print("Nomor Rekening:", Nasabah2.no_rekening)
print("Saldo:", Nasabah2.saldo)