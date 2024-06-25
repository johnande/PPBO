#No1b

class Passenger:
  TITLES = ("Mr", "Mrs", "Ms")

  def __init__(self, title, fname, lname):
    if title not in self.TITLES:
      raise ValueError("%s is not a valid title." % title)

    self.title = title
    self.fname = fname
    self.lname = lname

p1 = Passenger("Mr", "Kiewlamphone", "Souvanlith")
print(p1.TITLES)
print(Passenger.TITLES)
print(p1.title)
