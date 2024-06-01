class Rekening:
    nama = None
    rekening = 0
    saldo = 0
    def __init__(self, nama:str, rekening:int, saldo:float) -> None:
        self.nama = nama
        self.rekening = rekening
        self.saldo = saldo

class Nasabah(Rekening):
    def data(self):
        data = f"""Data Nasabah:
        --> Nama\t: {self.nama}
        --> Rekening\t: {self.rekening}
        --> Saldo\t: {self.saldo}"""
        return data
    
nasabah1 = Nasabah("Budi", 5555, 500000)
nasabah2 = Nasabah("Wati", 6666, 2000000)
print(nasabah1.data())
print(nasabah2.data())



