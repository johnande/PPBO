def addgreeting(cls):
    def greeting(self):
        print(f"Hello, I am a {self.__class__.__name__}!")
    cls.greeting = greeting
    return cls

@addgreeting
class myclass:
    pass

obj = myclass()
obj.greeting()