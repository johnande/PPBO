class bentuk:
    def __init__(self, x):
        self.x = x

kotak = bentuk(5)
print(kotak.x)  

del kotak.x

print(kotak.x)  