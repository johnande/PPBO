#================================================================ Soal 1 
from abc import ABC, abstractclassmethod
import random

class Hero(ABC):
    def __init__(self, name, attack, hp):
        self.name = name
        self.attack = attack
        self.hp = hp
    @abstractclassmethod
    def active_skill(self):
        pass
    @abstractclassmethod
    def passive_skill(self):
        pass
    @abstractclassmethod
    def ulti(self):
        pass
class Marksman(Hero):
    def active_skill(self, enemy):
        critical = self.passive_skill()
        damage = int(self.attack*critical)
        enemy.hp -= damage
        print(f"{self.name} deals damage {damage}, to {enemy.name}")
        print(f"{self.name} HP Remains {enemy.hp}")
    def passive_skill(self):
        return 1.0 + random.random()
    def ulti(self):
        pass
class Tank(Hero):
    def active_skill(self, enemy):
        heal = int(self.passive_skill()*self.hp)
        self.hp += heal #self.hp = self.hp + self.heal 
        enemy.hp -= self.attack
        print(f"{self.name} heals {heal}, current HP {self.hp}")
        print(f"{self.name} deals damage {self.attack} to {enemy.name}")
        print(f"{self.name} HP Remains {enemy.hp}")
    def passive_skill(self):
        return random.random()*3
    def ulti(self):
        pass

balmond = Tank("Balmond", 100, 2500)
layla = Marksman("Layla", 210, 1600)
arthur = Hero("Arthur", 250, 1000)

print("=== Turn 1 ===")
layla.active_skill(balmond)
print("=== Turn 2 ===")
balmond.active_skill(layla)
print("=== Turn 3 ===")
arthur.active_skill(balmond)

#================================================================ Soal 2
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
        print(f"Mobil Sedan ini adalah {self.merek} {self.model}, diproduksi tahun {self.tahun}.")

class SUV(Mobil):
    def display_info(self):
        print(f"Mobil SUV ini adalah {self.merek} {self.model}, diproduksi tahun {self.tahun}.")

class Hatchback(Mobil):
    def display_info(self):
        print(f"Mobil Hatchback ini adalah {self.merek} {self.model}, diproduksi tahun {self.tahun}.")

# Polimorfisme
def display_mobil(mobil):
    mobil.display_info()

# Contoh penggunaan
toyota_camry = Sedan('Toyota', 'Camry', 2021)
display_mobil(toyota_camry)

honda_crv = SUV('Honda', 'CR-V', 2020)
display_mobil(honda_crv)

suzuki_swift = Hatchback('Suzuki', 'Swift', 2019)
display_mobil(suzuki_swift)