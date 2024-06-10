class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        pass

class Kambing(Hewan):
    def suara(self):
        return "Mbekk"

class Ayam(Hewan):
    def suara(self):
        return "Kukuruyuk"

def main():
    kambing = Kambing("sheep")
    ayam = Ayam("chicken")

    print(f"{kambing.nama} bersuara: {kambing.suara()}")  
    print(f"{ayam.nama} bersuara: {ayam.suara()}")  

if __name__ == "__main__":
    main()

