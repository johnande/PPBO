class Motor:
  def __init__(self, merek):
    self.merek = merek

  def intro(self):
    print(f"Ini adalah motor {self.merek}.")

  def warna(self):
    print(f"{self.merek} ini berwana biru")

class Scoopy(Motor):
  def __init__(self):
    super().__init__("Scoopy")

  def warna(self):
    print(f"Motor {self.merek} berwarna putih")

class Beat(Motor):
  def __init__(self):
    super().__init__("Beat")

  def warna(self):
    print(f"Motor {self.merek} berwarna hitam")

scoopy = Scoopy()
beat = Beat()

scoopy.intro()
scoopy.warna()

beat.intro()
beat.warna()