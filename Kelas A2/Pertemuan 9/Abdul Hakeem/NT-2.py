from collections import namedtuple

orang = namedtuple("orang", "nama anak")

john = orang("John Doe", ["Jimmy", "Johnson"])

print(john)
print(id(john.anak))

john.anak.append("Tina")

print(john)
print(id(john.anak))


