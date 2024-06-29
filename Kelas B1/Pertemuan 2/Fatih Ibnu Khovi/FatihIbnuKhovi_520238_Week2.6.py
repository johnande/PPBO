class manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    
    def biodata(self):
        print("Nama anda " + self.nama)
        print("Umur anda " + str(self.umur))
    
def main():
    nama = input("Masukan Nama: ")
    umur = int(input("Masukan Umur: "))
    human = manusia(nama, umur)
    human.biodata()

if __name__ == "__main__":
    main()