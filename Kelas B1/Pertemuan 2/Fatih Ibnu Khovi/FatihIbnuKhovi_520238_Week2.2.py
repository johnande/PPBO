class segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
    
    def rumus(self):
        return (self.alas * self.tinggi) / 2

segitiga1 = segitiga(10, 20)

print(segitiga1.rumus())