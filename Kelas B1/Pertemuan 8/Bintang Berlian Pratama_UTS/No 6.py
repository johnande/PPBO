class Rekening():
    def __init__(self, nama, norek, saldo):
        self.nama = str(nama)
        self.norek = int(norek)
        self.saldo = float(saldo)
    def Setor_tunai(self, nominal):
        self.saldo = self.saldo + nominal
        print(f"Setor saldo sebesar {nominal} ke rekening {self.norek} berhasil")    
    def Tarik_tunai(self, nominal):
        if self.saldo < nominal:
            print("Saldo tidak mencukupi")
        else:
            self.saldo = self.saldo - nominal
            print(f"Penarikan saldo sebesar {nominal} dari rekening {self.norek} berhasil")
    def Transfer(self, penerima, nominal):
        if self.saldo < nominal:
            print("Saldo tidak mencukupi")
        else:
            self.saldo = self.saldo - nominal
            penerima.saldo = penerima.saldo + nominal
            print(f"Transfer sebesar {nominal} dari rekening {self.norek} ke rekening {penerima.norek} berhasil")

class Nasabah(Rekening):
    def __init__(self, nama, norek, saldo):
        super().__init__(nama, norek, saldo)
    def menampilkan_data(self):
        print(f"Nama: {self.nama}")
        print(f"Nomor Rekening: {self.norek}")
        print(f"Saldo: {self.saldo}\n")

nasabah1 = Nasabah("Budi",5555,500000)
nasabah2 = Nasabah("Wati",6666,2000000)

print("Nasabah 1")
nasabah1.menampilkan_data()
print("Nasabah 2")
nasabah2.menampilkan_data()

nasabah1.Setor_tunai(1000000)
nasabah2.Tarik_tunai(1000000)

print("\nSaldo setelah setor dan tarik tunai:")
print("Nasabah 1")
nasabah1.menampilkan_data()
print("Nasabah 2")
nasabah2.menampilkan_data()

nasabah1.Transfer(nasabah2,500000)

print("\nSaldo setelah transfer:")
print("Nasabah 1")
nasabah1.menampilkan_data()
print("Nasabah 2")
nasabah2.menampilkan_data()