class Laptop:
    def __init__(self, merek, processor):
        self.merek = merek
        self.processor = processor

    def info_laptop(self):
        print("Laptop", self.merek, "memiliki processor", self.processor)

laptop1 = Laptop("HP", "Intel Core i7 gen 8")
laptop2 = Laptop("DELL", "Intel Core i5 gen 9")

laptop1.info_laptop()
laptop2.info_laptop()