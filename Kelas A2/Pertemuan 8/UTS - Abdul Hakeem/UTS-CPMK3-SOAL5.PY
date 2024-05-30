class rekening():
    def __init__(self, name:str, accnum:int, balance:float):
        self.name = name
        self.accnum = accnum
        self.balance = balance

class customer(rekening):
    def __init__(self, name, accnum, balance):
        super().__init__(name, accnum, balance)
        
    def showdata(self):
        print(f"Nama: {self.name}")
        print(f"No. Rekening: {self.accnum}")
        print(f"Saldo: {self.balance}\n")
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Saldo setelah setor: {self.balance}\n")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Saldo tidak mencukupi")
        else:
            self.balance -= amount
            print(f"Saldo setelah tarik: {self.balance}\n")
    


nasabah1 = customer("Budi", 5555, 500000)
nasabah2 = customer("Wati", 6666, 2000000)

nasabah1.showdata()
nasabah2.showdata()

nasabah1.deposit(1000000)
nasabah2.withdraw(1000000)

nasabah1.showdata()
nasabah2.showdata()