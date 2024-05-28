class BentukGeometris:
    def __init__(self, nama):
        self.nama = nama

    def hitungLuas(self):
        pass


class PersegiPanjang(BentukGeometris):
    def __init__(self, nama, panjang, lebar):
        super().__init__(nama)
        self.panjang = panjang
        self.lebar = lebar

    def hitungLuas(self):
        return self.panjang * self.lebar


class Lingkaran(BentukGeometris):
    def __init__(self, nama, jari_jari):
        super().__init__(nama)
        self.jari_jari = jari_jari

    def hitungLuas(self):
        return 3.14 * self.jari_jari**2


def main():
    persegi_panjang = PersegiPanjang("Persegi Panjang", 4, 6)
    lingkaran = Lingkaran("Lingkaran", 5)

    daftar_bentuk = [persegi_panjang, lingkaran]

    for bentuk in daftar_bentuk:
        print(f"{bentuk.nama} - Luas: {bentuk.hitungLuas()}")


if __name__ == "__main__":
    main()
