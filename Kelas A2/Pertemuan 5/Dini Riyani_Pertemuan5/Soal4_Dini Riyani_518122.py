class Pembayaran_Parkir:
    def __init__(self, rate_per_jam):
        self.rate_per_jam = rate_per_jam

    def Perhitungan_Pembayaran(self, jam):
        return self.rate_per_jam * jam

    def __mul__(self, jam):
        return self.Perhitungan_Pembayaran(jam)

    def __str__(self):
        return "Rate per jam: Rp{}".format(self.rate_per_jam)

sistem_parkir = Pembayaran_Parkir(3000)  # Tarif parkir per jam: Rp3000
print(sistem_parkir)

jam_terparkir = 3
total_pembayaran = sistem_parkir * jam_terparkir
print("Total pembayaran untuk {} jam parkir: ${}".format(jam_terparkir, total_pembayaran))