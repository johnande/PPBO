from collections import namedtuple

Ninja = namedtuple("Ninja", "name quality attack defense")

kawaki = Ninja("Kawaki", 201.1, 234, 220)
himawari = Ninja("Himawari", 176.7, 192, 197)
kinshiki = Ninja("Kinshiki", 199.9, 223, 228)

ninja = [kawaki, himawari, kinshiki]

for i in ninja:
    print(f"Name: {i.name}")
    print(f"Quality: {i.quality}")
    print(f"Attack: {i.attack}")
    print(f"Defense: {i.defense}")
    print()