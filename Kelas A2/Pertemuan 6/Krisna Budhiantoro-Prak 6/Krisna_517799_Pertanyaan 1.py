class Passenger:

    TITLES = ("Mr", "Mrs", "Ms")

    def __init__(self, title, fname, lname):
        self.title = title
        self.fname = fname
        self.lname = lname

p1 = Passenger("Mr", "Kiewlamphone", "Souvanlith")

print(p1.TITLES)
print(Passenger.TITLES)
print(p1.title)
print(Passenger.title)
