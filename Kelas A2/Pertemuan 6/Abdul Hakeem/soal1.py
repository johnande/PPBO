from abc import ABC, abstractmethod
import random

class hero(ABC):
    def __init__(self, name, attack, hp):
        self.name = name
        self.attack = attack
        self.hp = hp

    @abstractmethod
    def act(self):
        pass

    @abstractmethod
    def pas(self):
        pass

    @abstractmethod
    def ult(self):
        pass

class mm(hero):
    def act(self, enemy):
        crit = self.pas()
        dmg = int(self.attack * crit)
        enemy.hp -= dmg
        print(f"{self.name} deals {dmg} damage to {enemy.name}")
        print(f"{enemy.name} has {enemy.hp} hp left")

    def pas(self):
        return 1.0 + random.random()
    
    def ulti(self):
        pass

class tank(hero):
    def act(self, enemy):
        heal = int(self.pas() * self.hp)
        self.hp += heal
        enemy.hp -= self.attack
        print(f"{self.name} heals {heal}, current HP is {self.hp}")
        print(f"{self.name} deals {self.attack} damage to {enemy.name}")
        print(f"{enemy.name} has {enemy.hp} hp left")

    def pas(self):
        return random.random() * 0.3
    
    def ult(self):
        pass

balmond = tank("Balmond", 100, 2500)
layla = mm("Layla", 210, 1600)

print("=== Round 1 ===")
layla.act(balmond)

print("=== Round 2 ===")
balmond.act(layla)