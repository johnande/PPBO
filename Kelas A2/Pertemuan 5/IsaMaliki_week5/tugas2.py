class Animal:
    def speak(self):
        pass


class Cat(Animal):
    def speak(self):
        print("Meow!")


class Cow(Animal):
    def speak(self):
        print("Moo!")


cat = Cat()
cow = Cow()

cat.speak()
cow.speak()


