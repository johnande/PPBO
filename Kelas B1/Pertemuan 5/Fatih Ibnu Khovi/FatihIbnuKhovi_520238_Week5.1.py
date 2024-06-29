class orang:
    def __init__(self, nama):
        self.nama = nama

    def prodi(self):
        pass

class fatih(orang):
    def prodi(self):
        return "Teknologi Rekayasa Internet"

class ibnu(orang):
    def prodi(self):
        return "Computer Science"


def main():
    Fatih = fatih("Fatih")
    Ibnu = ibnu("Ibnu")
 
    semua_orang = [Fatih, Ibnu]

    for orang in semua_orang:
        print(f"{orang.nama} sedang menempuh program studi {orang.prodi()}")

if __name__ == "__main__":
    main()