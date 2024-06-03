class LogDecorator:
    def __init__(self, original_class):
        self.original_class = original_class

    def __call__(self, *args, **kwargs):
        print(f"Memulai logging untuk {self.original_class.__name__}")
        return self.original_class(*args, **kwargs)

@LogDecorator
class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

calc = Calculator()

result_add = calc.add(5, 3)
result_sub = calc.subtract(10, 4)

print("Hasil penjumlahan:", result_add)
print("Hasil pengurangan:", result_sub)

