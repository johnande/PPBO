# IMPORTANT: ZIP THIS FILE. NOT THE OTHER ONE #
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
        print(f"Saldo {self.name} setelah setor: {self.balance}\n")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Saldo tidak mencukupi")
        else:
            self.balance -= amount
            print(f"Saldo {self.name} setelah tarik: {self.balance}\n")
    
    def transfer(self, recepient, amount):
        if amount > self.balance:
            print("Saldo tidak mencukupi")
        else:
            self.balance -= amount
            recepient.balance += amount
            print(f"Transfer dari {self.name} ke {recepient.name} sebesar {amount} telah berhasil.\n")
            print(f"Saldo {self.name} setelah transfer: {self.balance}\n")
            print(f"Saldo {recepient.name} setelah transfer: {recepient.balance}\n")
    


nasabah1 = customer("Budi", 5555, 500000)
nasabah2 = customer("Wati", 6666, 2000000)

nasabah1.showdata()
nasabah2.showdata()

methodchoice = int(input("Pilih metode untuk didemonstrasikan:\n1. Setor dan Tarik\n2. Transfer\n"))

if methodchoice == 1:
    nasabah1.deposit(1000000)
    nasabah2.withdraw(1000000)
    nasabah1.showdata()
    nasabah2.showdata()
elif methodchoice == 2:
    nasabah1.transfer(nasabah2, 500000)
    nasabah1.showdata()
    nasabah2.showdata()
else:
    print("Pilihan tidak valid")