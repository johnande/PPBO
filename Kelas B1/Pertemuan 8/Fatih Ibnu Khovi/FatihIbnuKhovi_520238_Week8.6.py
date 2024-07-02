class Rekening:
    def __init__(self, nama, no_rekening, saldo):
        self.nama = nama
        self.no_rekening = no_rekening
        self.saldo = saldo
    
    def Setor_tunai(self, tunai):
        self.saldo += tunai
        print("Setor Tunai Telah Berhasil")
        print("Saldo: ", self.saldo)
    
    def Tarik_tunai(self, tunai):
        if self.saldo >= tunai:
            self.saldo -= tunai
            print("Tarik Tunai Telah Berhasil")
            print("Saldo: ", self.saldo)
        else:
            print("Maaf Saldo Anda Tidak Mencukupi")
    
    def Transfer(self, penerima, tunai):
        if self.saldo >= tunai:
            self.saldo -= tunai
            penerima.saldo += tunai
            print("Transfer sebesar", tunai, "dari rekening", self.no_rekening, "ke rekening", penerima.no_rekening, "berhasil")
        else:
            print("Maaf Saldo Anda Tidak Mencukupi")


class Nasabah(Rekening):
    def __init__(self, nama, no_rekening, saldo):
        super().__init__(nama, no_rekening, saldo)

Nasabah1 = Nasabah("Budi", int(5555), float(500000))
Nasabah2 = Nasabah("Wati", int(6666), float(2000000))

print("Informasi Nasabah 1")
print("Nama:", Nasabah1.nama)
print("Nomor Rekening:", Nasabah1.no_rekening)
print("Saldo:", Nasabah1.saldo)

print(" ")

print("Informasi Nasabah 2")
print("Nama:", Nasabah2.nama)
print("Nomor Rekening:", Nasabah2.no_rekening)
print("Saldo:", Nasabah2.saldo)

print(" ")

print("Transaksi ATM")
Nasabah1.Setor_tunai(float(1000000)) 
Nasabah2.Tarik_tunai(float(1000000))

print(" ")

print("Informasi Nasabah 1")
print("Nama:", Nasabah1.nama)
print("Nomor Rekening:", Nasabah1.no_rekening)
print("Saldo:", Nasabah1.saldo)

print(" ")

print("Informasi Nasabah 2")
print("Nama:", Nasabah2.nama)
print("Nomor Rekening:", Nasabah2.no_rekening)
print("Saldo:", Nasabah2.saldo)

print(" ")

print("Transaksi Transfer")
Nasabah1.Transfer(Nasabah2, float(500000))

print(" ")

print("Informasi Nasabah 1")
print("Nama:", Nasabah1.nama)
print("Nomor Rekening:", Nasabah1.no_rekening)
print("Saldo:", Nasabah1.saldo)

print(" ")

print("Informasi Nasabah 2")
print("Nama:", Nasabah2.nama)
print("Nomor Rekening:", Nasabah2.no_rekening)
print("Saldo:", Nasabah2.saldo)