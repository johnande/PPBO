class orang:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def status (self):
        print(f"Name\t: {self.name}\nAge\t: {self.age}\nStatus\t: Unknown")

class student(orang):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)

    def status(self):
        print(f"Name\t: {self.name}\nAge\t: {self.age}\nStatus\t: Student")

orang1 = orang("Budi", 20)
orang1.status()

print()

student1 = student("Andi", 19)
student1.status()

