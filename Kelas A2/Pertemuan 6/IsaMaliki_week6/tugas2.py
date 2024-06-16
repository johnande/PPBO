from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
    
    @abstractmethod
    def basic_attack(self):
        pass

    @abstractmethod
    def skill(self):
        pass

class Astro(Hero):
    def basic_attack(self, enemy):
        damage = self.attack * 1.4
        enemy.hp -= damage
        print(f"{self.name} memmberikan {damage:.2f} serangan ke {enemy.name}")
        print(f"{enemy.name} memiliki sisa {enemy.hp} HP")
        print()

    def skill(self):
        pass


class Mage(Hero):
    def basic_attack(self):
        pass

    def skill(self,enemy):
        damage = self.attack * 0.6
        heal = damage * 0.1
        self.hp += heal
        enemy.hp -= damage
        print(f"{self.name} memberikan {damage:.2f} serangan ke {enemy.name}")
        print(f"{self.name} mendapatkan {heal} HP tambahan")
        print(f"{enemy.name} memiliki sisa {enemy.hp} HP")
        print()

irithel = Astro("Irithel", 10745, 730)
valentina = Mage("Valentina", 10530, 895)

irithel.basic_attack(valentina)
valentina.skill(irithel)

print(f"HP akhir {irithel.name} adalah {irithel.hp}")
print(f"HP akhir {valentina.name} adalah {valentina.hp}")