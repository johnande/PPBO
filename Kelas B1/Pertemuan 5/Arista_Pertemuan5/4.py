class JadwalPiket:
    def __init__(self, hari, jam):
        self.hari = hari
        self.jam = jam

    def __str__(self):
        return f"Piket pada hari {self.hari}, pukul {self.jam}"

    def __add__(self, other):
        return JadwalPiket(self.hari + " dan " + other.hari, self.jam + " serta " + other.jam)

senin = JadwalPiket("Senin", "08.00-10.00")
selasa = JadwalPiket("Selasa", "10.00-12.00")
rabu = JadwalPiket("Rabu", "12.00-14.00")

gabungan = senin + selasa + rabu
print(gabungan)
