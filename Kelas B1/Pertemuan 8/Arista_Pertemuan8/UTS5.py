class Rekening:
    def __init__(self, nama, no_rekening, saldo):
        self.nama = nama
        self.no_rekening = no_rekening
        self.saldo = saldo
    
    def tambah_saldo(self, jumlah):
        self.saldo += jumlah
    
    def tarik_saldo(self, jumlah):
        if jumlah <= self.saldo:
            self.saldo -= jumlah
            print("Tarik tunai berhasil.")
        else:
            print("Saldo tidak mencukupi untuk melakukan penarikan.")
    
    def setor(self, jumlah):
        self.tambah_saldo(jumlah)
        print("Setor tunai berhasil.")

class Nasabah(Rekening):
    def display_data(self):
        print("*" * 37)
        print("*" + " " * 35 + "*")
        print("*" + " " * 7 + "Data Nasabah Bank" + " " * 7 + "*")
        print("*" + " " * 35 + "*")
        print("*" + " Nama : " + self.nama + " " * (21 - len(self.nama)) + "*")
        print("*" + " No. Rek : " + str(self.no_rekening) + " " * (21 - len(str(self.no_rekening))) + "*")
        print("*" + " Saldo : " + str(self.saldo) + " " * (21 - len(str(self.saldo))) + "*")
        print("*" + " " * 35 + "*")
        print("*" * 37)
    
    def setor(self, jumlah):
        super().setor(jumlah)
    
    def tarik(self, jumlah):
        super().tarik_saldo(jumlah)

nasabah1 = Nasabah("Budi", 5555, 500000)
nasabah2 = Nasabah("Wati", 6666, 2000000)

nasabah1.setor(1000000)
nasabah2.tarik(1000000)

print("Data Nasabah Setelah Transaksi:")
nasabah1.display_data()
nasabah2.display_data()
