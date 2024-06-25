#No2

class Mobil:
    def __init__(self, merek):
        self.merek = merek

    def intro(self):
        print(f"Ini adalah mobil {self.merek}.")

    def bergerak(self):
        print(f"{self.merek} dapat bergerak dengan kecepatan tinggi.")

class Ferrari(Mobil):
    def __init__(self):
        super().__init__("Ferrari")

    def bergerak(self):
        print(f"{self.merek} melaju dengan kecepatan luar biasa.")

class BMW(Mobil):
    def __init__(self):
        super().__init__("BMW")

    def bergerak(self):
        print(f"{self.merek} menawarkan keseimbangan antara performa dan kenyamanan.")

ferrari = Ferrari()
bmw = BMW()

ferrari.intro()
ferrari.bergerak()

bmw.intro()
bmw.bergerak()
