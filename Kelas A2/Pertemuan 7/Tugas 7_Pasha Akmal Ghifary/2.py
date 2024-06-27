class Person:
    sehat = False

    def dinyatakan_sehat(self):
        self.sehat = True

joni = Person()
eko = Person()

joni.dinyatakan_sehat()
print("joni sehat : ", joni.sehat)
print("eko sehat: ", eko.sehat)