#No4

class Novel:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis

    def info(self):
        return f"Novel '{self.judul}' oleh {self.penulis}"

    def __add__(self, other):
        return f"{self.judul} dan {other.judul}"

novel1 = Novel("Harry Potter", "J.K. Rowling")
novel2 = Novel("Pride and Prejudice", "Jane Austen")

print(novel1.info())
print(novel2.info())

gabungan_judul = novel1 + novel2
print(f"Gabungan judul: {gabungan_judul}")
