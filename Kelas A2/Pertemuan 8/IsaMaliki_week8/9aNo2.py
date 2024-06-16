class Immortal:
    def __init__(self, name, base_damage, stacks):
        self.name = name
        self.base_damage = base_damage
        self.stacks = stacks

    def damage(self):
        return self.base_damage + 15 * self.stacks
    
    @property
    def damage_as_attribute(self):
        return self.base_damage + 15 * self.stacks
    
    @classmethod
    def damage_as_classmethod(cls, base_damage, stacks):
        return base_damage + 15 * stacks
    
    @staticmethod
    def damage_as_staticmethod(base_damage, stacks):
        return base_damage + 15 * stacks
    
gatotkaca = Immortal("Gatotkaca", 2000, 15)

print("Metode objek")
print(gatotkaca.damage())

print("\nPenggunaan @property")
print(gatotkaca.damage_as_attribute)

print("\nMetode Kelas")
print(gatotkaca.damage_as_classmethod(gatotkaca.base_damage, gatotkaca.stacks))
print(Immortal.damage_as_classmethod(2000,15))

print("\nMetode static")
print(gatotkaca.damage_as_staticmethod(gatotkaca.base_damage, gatotkaca.stacks))
print(Immortal.damage_as_staticmethod(2000,15))