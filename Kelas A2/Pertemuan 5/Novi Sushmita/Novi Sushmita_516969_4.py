class Bulanan:
    def __init__(self, total_uang):
        self.total_uang = total_uang

    def __sub__(self, pengeluaran_harian):
        return self.total_uang - pengeluaran_harian.jumlah_pengeluaran

class Harian:
    def __init__(self, nama_pengeluaran, jumlah_pengeluaran):
        self.nama_pengeluaran = nama_pengeluaran
        self.jumlah_pengeluaran = jumlah_pengeluaran

bulan_januari = Bulanan(100000)
hari_1 = Harian("bensin", 10000)

print(f"Sisa uang bulan Januari setelah pengeluaran {hari_1.nama_pengeluaran}: {bulan_januari-hari_1} ribu")