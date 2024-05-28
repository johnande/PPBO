class Binatang:
    def __init__(self, nama):
        self.nama = nama

    def bersuara(self):
        pass


class Kucing(Binatang):
    def bersuara(self):
        return "Meow"


class Anjing(Binatang):
    def bersuara(self):
        return "Woof"


class Bebek(Binatang):
    def bersuara(self):
        return "Quack"


def main():
    kucing = Kucing("Kitty")
    anjing = Anjing("Buddy")
    bebek = Bebek("Donald")

    daftar_binatang = [kucing, anjing, bebek]

    for binatang in daftar_binatang:
        print(f"{binatang.nama} bersuara: {binatang.bersuara()}")


if __name__ == "__main__":
    main()
