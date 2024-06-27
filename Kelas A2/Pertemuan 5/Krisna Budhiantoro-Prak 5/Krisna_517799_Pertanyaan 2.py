class Tank(Hero):
    def active_skill(self, enemy):
        heal = int(self.passive_skill() * self.hp)
        self.hp += heal
        enemy.hp -= self.attack
        print(f"{self.name} heals {heal}, current HP {self.hp}")
        print(f"{self.name} deals damage {self.attack} to {enemy.name}")
        print(f"{enemy.name} HP remains {enemy.hp}")

    def passive_skill(self):
        return random.random() * 0.3

    def ulti(self):
        pass

# Mencoba membuat objek dari kelas Hero
# Ini akan menghasilkan error karena Hero adalah kelas abstrak
hero = Hero("Hero", 100, 2000)
