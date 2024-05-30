class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Decorator called")
        return self.func(*args, **kwargs)

@Decorator
def say_something():
    print("Keep Fighting Bro!")

say_something()