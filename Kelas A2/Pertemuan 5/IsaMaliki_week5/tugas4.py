class Hero:
    def __init__(self, hero, base_hp):
        self.hero = hero
        self.base_hp = base_hp

    def __add__(self, addition):
        return self.base_hp + addition.num_hp
    
class Guardian:
    def __init__(self, hero, num_hp):
        self.hero = hero
        self.num_hp = num_hp #jumlah hp tambahan

belerick = Hero("Belerick", 3310)
heroes_2 = Guardian("Belerick", 400)
print(f"Total Health Point {belerick.hero} : {belerick+heroes_2}")

