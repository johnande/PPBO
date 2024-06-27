class Melon :
  def rasa(self):
    print("Manis")

  def bentuk(self):
    print("Bulat")

  def __str__(self):
    return "Melon"

class Belimbing :
  def rasa(self):
    print("Kecut")

  def bentuk(self):
    print("Bintang")

  def __str__(self):
    return "Belimbing"

melon = Melon()
belimbing = Belimbing()

for buah in (melon, belimbing):
  print(f"Rasa dari {buah} adalah ", end="")
  buah.rasa()
  print(f"Bentuk dari {buah} adalah ", end="")
  buah.bentuk()