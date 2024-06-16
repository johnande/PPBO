class Astro:
    def __init__(self, name, base_damage):
        self.name = name
        self.base_damage = base_damage

    def damage(self):
        total_damage = 1.4 * self.base_damage
        print(f"Hero's Name = {self.name}\nTotal Damage = {total_damage}")


class Immortal:
    def __init__(self, name, stack):
        self.name = name
        self.stack = stack

    def damage(self):
        total_damage = self.stack * 35
        print(f"Hero's Name = {self.name}\nTotal Damage = {total_damage}")

lancelot = Astro("Lancelot",500)
lancelot.damage()

karina = Immortal("Karina", 25)
karina.damage()

