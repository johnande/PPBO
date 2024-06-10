class Passenger :
    TITLES=("Mr","Mrs", "Ms")

    def __init__(self, title, fname, lname):
        if title not in self.TITLES:
            raise ValueError("%s is not a valid title." %title)
        
        self.title=title #intance attribute
        self.fname=fname #intance attribute
        self.lname=lname #intance attribute

#pembuatan attribute
p1=Passenger( "Mr", "Kiewlamphone","Souvanlith")
#mengakses class attribute dari object
print(p1.TITLES)
#mengakses class attribute dari kelas
print(Passenger.TITLES)
#mengakses instance attribute dari object
print(p1.title)
#mengakses instance attribute dari kelas
print(Passenger.title)

