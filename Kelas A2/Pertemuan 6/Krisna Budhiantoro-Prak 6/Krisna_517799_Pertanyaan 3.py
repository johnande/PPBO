def add_greeting(cls):

    def greeting(self):
        print("Hello, I am a {self._class_._name_}!")

    cls.greeting = greeting

    return cls


@add_greeting
class MyClass:
    pass


obj = MyClass()
obj.greeting()
