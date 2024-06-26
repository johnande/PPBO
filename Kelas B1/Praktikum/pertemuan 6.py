#================================================ Soal 1
class Passenger:
    TITLES = ("Mr", "Mrs", "Ms") 
    def __init__ (self, title, fname, lname):
        if title not in self.TITLES:
            raise ValueError ("%s is not valis title." %title)
        self.title = title
        self.fname = fname
        self.lname = lname
p1 = Passenger ("Mr", "Kiewlamphone", "Souvanlith")
print(p1.TITLES)
print(Passenger.TITLES)
print(p1.title)
print(Passenger.title)

#=============================================== Soal 2
class Person:
    sehat = False
    
    def dinyatakan_sehat(self):
        self.sehat = True

joni = Person()
eko = Person()

joni.dinyatakan_sehat()
print("Joni sehat: ", joni.sehat)
print("Eko sehat: ", eko.sehat)

#=============================================== Soal 3
def add_greeting(cls):
    def greeting(self):
        print(f"Hello, I am a {self.__class__.__name__}!")
    cls.greeting = greeting
    return cls

@add_greeting
class MyClass:
    pass

obj = MyClass()
obj.greeting()  

#=============================================== Soal 4
def mobil_decorator(fungsi_mobil):
    def intro(*args, **kwargs):
        print("Ini adalah mobil yang luar biasa!")
        fungsi_mobil(*args, **kwargs)
        print("Mobil yang sangat cepat!")
    return intro

@mobil_decorator
def tampilkan_mobil(nama):
    print(f"Mobil ini adalah {nama}.")

tampilkan_mobil("Lamborgini Huracan")
