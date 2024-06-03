class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

# Membuat objek dengan konstruktor
car1 = Car("Toyota", "Camry", 2022)

# Memanggil metode untuk menampilkan informasi mobil
car1.display_info()
