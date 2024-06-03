class MyDecorator:
    def __init__(self, original_class):
        self.original_class = original_class

    def __call__(self, *args, **kwargs):
        instance = self.original_class(*args, **kwargs)
        print(f"Menjalankan class {self.original_class.__name__}")
        return instance

@MyDecorator
class MyClass:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, {self.name}!")

my_instance = MyClass("John")
my_instance.say_hello()
