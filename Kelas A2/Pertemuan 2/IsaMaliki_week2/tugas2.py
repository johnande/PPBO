class hero:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def print_hero(self):
        print(f"{self.name} is a {self.role}")


hero1 = hero("Miya", "Marksman")
hero2 = hero("Layla", "Marksman")
hero3 = hero("Eudora", "Mage")

hero1.print_hero()
hero2.print_hero()
hero3.print_hero()