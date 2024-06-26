#================================================================ Soal 1
mil = float(input("Masukkan angka dalam satuan Mil= "))
kilometer = mil * 1.60934
print(f"{mil} mil = {kilometer} kilometer")

#================================================================ Soal 3
from abc import ABC, abstractmethod

class Mobil(ABC):
    def __init__(self, merek, model, tahun):
        self.merek = merek
        self.model = model
        self.tahun = tahun
        
    @abstractmethod
    def display_info(self):
        pass
 
class Sedan(Mobil):
    def display_info(self):
        print(f"Mobil Sedan ini adalah {self.merek} {self.model}, produksi tahun {self.tahun}.")
class SUV(Mobil):
    def display_info(self):
        print(f"Mobil SUV ini adalah {self.merek} {self.model}, produksi tahun {self.tahun}.")
class Hatchback(Mobil):
    def display_info(self):
        print(f"Mobil Hatchback ini adalah {self.merek} {self.model}, produksi tahun {self.tahun}.")

def display_info(mobil):
    mobil.display_info()
    
toyota_camry = Sedan("Toyota", "Camry", 2021)  
display_info(toyota_camry)    
bmw_X3 = SUV("BMW", "X3", 2024)
display_info(bmw_X3)
mazda_3 = Hatchback("Mazda", "3", 2024)
display_info(mazda_3)

#================================================================ Soal 4
class Rekening:
    def __init__(self, nama, no_rekening, saldo):
        self.nama = nama
        self.no_rekening = no_rekening  
        self.saldo = float(saldo)  

class Nasabah(Rekening):
    def display_info(self):
        print(f"Nama nasabah: {self.nama}")
        print(f"Nomor rekening: {self.no_rekening}")
        print(f"Saldo: {self.saldo:,.2f}")

nasabah1 = Nasabah("Budi", 5555, 500000.0)
nasabah2 = Nasabah("Wati", 6666, 2000000.0)

print("Informasi Nasabah 1:")
nasabah1.display_info()

print("\nInformasi Nasabah 2:")
nasabah2.display_info()

#================================================================ Soal 5
class Rekening:
    def __init__(self, nama, no_rekening, saldo):
        self.nama = nama
        self.no_rekening = no_rekening  
        self.saldo = float(saldo)  
    def setor_tunai(self, jumlah):
        self.saldo += jumlah
        print(f"Transaksi berhasil. \nSaldo saat ini: Rp {self.saldo:,.2f}")
    def tarik_tunai(self, jumlah):
        if self.saldo >= jumlah:
            self.saldo -= jumlah
            print(f"Transaksi berhasil. \nSaldo saat ini: Rp {self.saldo:,.2f}")
        else:
            print(f"Transaksi Gagal, saldo tidak mencukupi. \nSaldo saat ini: Rp {self.saldo:,.2f}")

class Nasabah(Rekening):
    def display_info(self):
        print(f"Nama nasabah: {self.nama}")
        print(f"Nomor rekening: {self.no_rekening}")
        print(f"Saldo: Rp {self.saldo:,.2f}")
        
#objek nasabah
nasabah1 = Nasabah("Budi", 5555, 500000)
nasabah2 = Nasabah("Wati", 6666, 2000000)
print("Informasi Nasabah 1:")
nasabah1.display_info()
print("\nInformasi Nasabah 2:")
nasabah2.display_info()

#simulasi transaksi
print("\nInformasi transaksi Nasabah 1:")
nasabah1.setor_tunai(1000000)
print("\nInformasi transaksi Nasabah 2:")
nasabah2.tarik_tunai(1000000)
#================================================================ Soal 6
class Rekening:
    def __init__(self, nama, no_rekening, saldo):
        self.nama = nama
        self.no_rekening = no_rekening  
        self.saldo = float(saldo)  
    def setor_tunai(self, jumlah):
        self.saldo += jumlah
        print(f"Transaksi berhasil. \nSaldo saat ini: Rp {self.saldo:,.2f}")
    def tarik_tunai(self, jumlah):
        if self.saldo >= jumlah:
            self.saldo -= jumlah
            print(f"Transaksi berhasil. \nSaldo saat ini: Rp {self.saldo:,.2f}")
        else:
            print(f"Transaksi Gagal, saldo tidak mencukupi. \nSaldo saat ini: Rp {self.saldo:,.2f}")
    def transfer(self, penerima, jumlah):
        if self.saldo >= jumlah:
            self.saldo -= jumlah
            penerima.saldo += jumlah
            print(f"""Transaksi berhasil.\nPenerima: {penerima.nama} \nNomor Rekening: {penerima.no_rekening} \nJumlah transaksi: Rp {jumlah:,.2f}  
                  \nSaldo saat ini: Rp {self.saldo:,.2f}""")
        else:
            print(f"Transaksi Gagal, periksa saldo dan nomor rekening tujuan. \nSaldo saat ini: Rp {self.saldo:,.2f}")
            
class Nasabah(Rekening):
    def display_info(self):
        print(f"Nama nasabah: {self.nama}")
        print(f"Nomor rekening: {self.no_rekening}")
        print(f"Saldo: Rp {self.saldo:,.2f}")

#objek nasabah
nasabah1 = Nasabah("Budi", 5555, 500000)
nasabah2 = Nasabah("Wati", 6666, 2000000)
print("Informasi Nasabah 1:")
nasabah1.display_info()
print("\nInformasi Nasabah 2:")
nasabah2.display_info()

#simulasi transaksi
print("\nInformasi transaksi Nasabah 1:")
nasabah1.setor_tunai(1000000)
print("\nInformasi transaksi Nasabah 2:")
nasabah2.tarik_tunai(1000000)

#simulasi transfer
print("\nInformasi transaksi:")
nasabah1.transfer(nasabah2, 500000)
