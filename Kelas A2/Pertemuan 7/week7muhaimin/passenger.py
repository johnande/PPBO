class Passenger:
    TITLES=("Mr","Mrs","Ms") #class attribute
    def __init__(self,title,fname,lname):
        if title not in self.TITLES:
            raise ValueError("%s is not a valid title." % title)
            
            self.title= title
            self.fname= fname
            self.lname= lname
            
#pembuatan objek
p1= Passenger("Mr","Kiewlamphone","Souvanlith")
#mengakses class dari attribute
print(p1.TITLES)
# mengakses class attribute
print(Passenger.TITLES)
# mengakses instance attribute dari objek
print(p1.title)
# mengakses instance attribute dari kelas
print(Passenger.TITLES)