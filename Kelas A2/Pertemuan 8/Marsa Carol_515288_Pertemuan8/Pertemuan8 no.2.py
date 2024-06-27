class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    @property
    def nama(self):
        return self._nama

    @nama.setter
    def nama(self, nilai):
        if not nilai:
            raise ValueError("Nama produk tidak boleh kosong")
        self._nama = nilai

    @property
    def harga(self):
        return self._harga

    @harga.setter
    def harga(self, nilai):
        if nilai < 0:
            raise ValueError("Harga tidak boleh negatif")
        self._harga = nilai

    @classmethod
    def harga_diskon(cls, harga, persentase_diskon):
        return harga * (1 - persentase_diskon / 100)

    @staticmethod
    def tambah_ppn(harga, tarif_ppn):
        return harga * (1 + tarif_ppn / 100)


# Contoh penggunaan
produk1 = Produk("Kaos", 100)
print("Produk:", produk1.nama)
print("Harga:", produk1.harga)

harga_diskon = Produk.harga_diskon(produk1.harga, 10)
print("Harga setelah Diskon:", harga_diskon)

harga_dengan_ppn = Produk.tambah_ppn(harga_diskon, 5)
print("Harga setelah Diskon dan ditambahkan PPN:", harga_dengan_ppn)
