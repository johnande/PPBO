from collections import namedtuple

def decorator_showinfo(func):
    def showinfo(self):
        print(f"Nama: {self.nama}")
        print("Anak:")
        for i in range(len(self.anak)):
            print(f"{i+1}. {self.anak}")
    func.showinfo = showinfo
    return func

@decorator_showinfo
class orang(namedtuple("orang", "nama anak")):
    pass

john = orang("John Doe", ["Jimmy", "Johnson"])

print(john)
print(id(john.anak))

john.anak.append("Tina")

print(john)
print(id(john.anak))

john.showinfo()


