class Rekening:
   
    def __init__(self, nama:str, rekening:int, saldo:float) -> None:
        self.nama = nama
        self.rekening = rekening
        self.saldo = saldo
    
    def tarik_tunai(self, jumlah:float):
        self.saldo -= jumlah
        print(f"nasabah {self.nama} telah melakukan tarik tunai sebesar {jumlah}")

    def setor_tunai(self, jumlah:float):
        self.saldo += jumlah
        print(f"nasabah {self.nama} telah melakukan setor tunai sebesar {jumlah}")

class Nasabah(Rekening):
    def data(self):
        data = f"""Data Nasabah:
        --> Nama\t: {self.nama}
        --> Rekening\t: {self.rekening}
        --> Saldo\t: {self.saldo}"""
        return data

nasabah1 = Nasabah("Budi", 5555, 500000)
nasabah2 = Nasabah("Wati", 6666, 2000000)
nasabah1.tarik_tunai(100000)
print(nasabah1.data())
print()
nasabah2.setor_tunai(500000)
print(nasabah2.data())

