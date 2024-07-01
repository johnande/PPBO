def add_hello(func):
    def wrapper(self):
        print("Hello,")
        return func(self)
    return wrapper

class MyClass:
    def __init__(self, name):
        self.name = name

    @add_hello
    def say_name(self):
        print(f"My name is {self.name}.")

obj = MyClass("Alice")
obj.say_name()
