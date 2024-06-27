class Monsters:
    def __init__(self,Nama, Darah):
        self.nama = Nama
        self.darah = Darah

Monster1 = Monsters("Maul", 1000)

print(Monster1.__dict__)