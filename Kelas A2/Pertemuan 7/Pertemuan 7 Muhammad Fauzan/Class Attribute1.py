class passenger:
    TITLES = ("Mr", "Mrs", "Ms") #class attribute

    def __init__(self, title, fname, lname):
        if title not in self.TITLES:
            raise ValueError("%s is not a valid title." % title)
        
        self.title = title #instance attribute
        self.fname = fname
        self.lname = lname

#pembuatan objek
P1 = passenger("Mr", "Kiewlamphone", "Souvanlith")
#mengakses class attribute dari object
print(P1.TITLES)
#mengakses class attribute dari kelas
print(passenger.TITLES)
#mengakses instance attribute dari objek
print(P1.title)
#mengakses instance attribute dari kelas
print(passenger.title)