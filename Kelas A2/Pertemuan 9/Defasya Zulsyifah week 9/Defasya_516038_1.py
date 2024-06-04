class Makanan:
    def _init_(self, nama, kalori):
        self.nama = nama
        self.kalori = kalori

    @property
    def nama(self):
        return self._nama

    @nama.setter
    def nama(self, nilai):
        if not nilai:
            raise ValueError("Nama makanan tidak boleh kosong")
        self._nama =  nilai

    @property
    def kalori(self):
        return self._kalori

    @kalori.setter
    def kalori(self, nilai):
        if nilai ≤ 0:
            raise ValueError("Kalori harus lebih besar dari @")
        self._kalori = nilai

    @classmethod
    def dari_resep(cls, resep):
        nama, kalori = resep.split(":")
        return cls(nama.strip(), int(kalori.strip()))

    @staticmethod
    def sehat(kalori):
        return kalori < 500

makanan1 = Makanan("Apel", 95)
print("Nana Makanan:", makanani.nana)
print("Kalori:", makanani.kalori)
print("Apakah makanan sehat?", "Ya" if
Makanan.sehat(makanan1.kalori) else "Tidak")

makanan2 = Makanan.dari_resep("Burger: 600")
print("\nNama Makanan:", makanan2.nama)
print("Kalori:", makanan2.kalori)
print("Apakah makanan sehat?", "Ya" if
Makanan.sehat(makanan2.kalori) else "Tidak")