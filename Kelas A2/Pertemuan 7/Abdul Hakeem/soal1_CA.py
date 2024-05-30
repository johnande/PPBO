class passenger:
    TITLES = ("Mr", "Mrs", "Ms")

    def __init__(self, title, fn, ln):
        if title not in self.TITLES:
            raise ValueError(f"Title must be one of {self.TITLES}")

        self.title = title
        self.fn = fn
        self.ln = ln

p1 = passenger("Mr", "Abdul", "Hakeem")

print(p1.TITLES)
print(passenger.TITLES)
print(p1.title)
print(passenger.title)