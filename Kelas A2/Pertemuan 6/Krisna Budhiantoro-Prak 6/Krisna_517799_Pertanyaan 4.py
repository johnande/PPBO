def add_prefix(cls):
    cls._name = "My" + cls.__name__
    return cls


@add_prefix
class MyClass:
    def __init__(self, x):
        self.x = x

    def display(self):
        print("Nilai x:", self.x)


obj = MyClass(5)
obj.display()
print("Nama kelas:", MyClass.__name__)
