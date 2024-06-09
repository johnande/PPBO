class Strenght:
    def __init__(self, hero, damage):
        self.hero = hero
        self.damage = damage
    
    def attack(self):
        total_attack = 2 * self.damage
        print(f"Nama = {self.hero}\n Damage total = {total_attack}")

class Magic:
    def __init__(self, hero, magic_damage):
        self.hero = hero
        self.magic_damage = magic_damage

    def magic(self):
        total_magic_damage = self.magic_damage * 2
        print(f"Nama = {self.hero}\n Damage total = {total_magic_damage}")
        
class Pshysical:
    def __init__(self, hero, Damage_hit):
        self.hero = hero
        self.Damage_hit = Damage_hit

    def hit(self):
        kena_hit = self.Damage_hit * 2
        print(f"Nama = {self.hero}\n Damage total = {kena_hit}")

Abandon = Pshysical("Abandon", 1000)
Abandon.hit()

Warlock = Magic("Warlock", 500)
Warlock.magic()

Pudge = Strenght("Pudge", 10000)
Pudge.attack()