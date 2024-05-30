class FruitCounter:
    _instance = None
    _count = 0

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def add_fruit(self):
        self._count += 1

    def get_count(self):
        return self._count

# Contoh penggunaan Singleton Pattern untuk menghitung jumlah buah
counter1 = FruitCounter()
counter1.add_fruit()

counter2 = FruitCounter()
counter2.add_fruit()

print(counter1.get_count())  # Output: 2
print(counter2.get_count())  # Output: 2
print(counter1 is counter2)  # Output: True, karena keduanya adalah instansi yang sama
