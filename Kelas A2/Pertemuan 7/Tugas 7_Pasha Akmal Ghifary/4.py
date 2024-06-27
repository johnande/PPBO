class SmartDivide:
    def __init__(self, func):
        self.func = func

    def __call__(self, a, b):
        print("Memproses pembagian:", a, "/", b)
        if b == 0:
            print("Oops! Tidak bisa membagi dengan nol.")
            return None
        return self.func(a, b)

@SmartDivide
def bagi(a, b):
    return a / b

hasil = bagi(10, 2)
print("Hasil pembagian:", hasil)

hasil = bagi(5, 0)
print("Hasil pembagian:", hasil)