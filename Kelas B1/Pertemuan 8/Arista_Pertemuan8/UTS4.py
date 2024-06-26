class Rekening:
    def __init__(self, nama, no_rekening, saldo):
        self.nama = nama
        self.no_rekening = no_rekening
        self.saldo = saldo

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

nasabah1 = Nasabah("Budi", 5555, 500000)
nasabah2 = Nasabah("Wati", 6666, 2000000)

print("Nasabah Bank:")
nasabah1.display_data()
nasabah2.display_data()
