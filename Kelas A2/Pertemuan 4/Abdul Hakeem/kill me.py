# Kelas induk atau superclass
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def speak(self):
        pass

# Kelas anak atau subclass yang mewarisi dari kelas Character
class Hero(Character):
    def __init__(self, name, health, weapon):
        super().__init__(name, health)
        self.weapon = weapon

    def speak(self):
        return f"I am {self.name}. I fight for justice with my {self.weapon}!"

# Kelas anak atau subclass yang mewarisi dari kelas Character
class Villain(Character):
    def __init__(self, name, health, evil_laugh):
        super().__init__(name, health)
        self.evil_laugh = evil_laugh

    def speak(self):
        return f"I am {self.name}. Prepare to be defeated by my {self.evil_laugh}!"

# Fungsi untuk memulai pertarungan antara pahlawan dan penjahat
def battle(hero, villain):
    print(f"{hero.name} encounters {villain.name}!")

    while hero.health > 0 and villain.health > 0:
        print(f"{hero.name} attacks {villain.name}!")
        villain.health -= 10
        print(f"{villain.name}'s health: {villain.health}")

        print(f"{villain.name} counterattacks!")
        hero.health -= 8
        print(f"{hero.name}'s health: {hero.health}")

    if hero.health <= 0:
        print(f"{villain.name} has defeated {hero.name}!")
    else:
        print(f"{hero.name} has defeated {villain.name}!")

# Membuat karakter-karakter untuk pertarungan
hero = Hero("Superman", 100, "super powers")
villain = Villain("Lex Luthor", 120, "diabolical laugh")

# Memulai pertarungan
battle(hero, villain)   