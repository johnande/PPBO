class Passsenger:

    TITLES = ('Mr', 'Mrs', 'Ms') # class attribute

    def __init__(self, title, fname, lname):
        if title not in self.TITLES:
            raise ValueError("%s is not a valid title." % title)
        self.title = title
        self.fname = fname
        self.lname = lname

p1 = Passsenger('mr', 'Kiewlamphone', 'Souvanlith')
print(p1.TITLES)
print(Passsenger.TITLES)
print(p1.title)
# print(Passsenger.title)