class Bilangan:
    def __init__(self, nilai):
        self.nilai = nilai

    def __pow__(self, pangkat):
        return self.nilai ** pangkat


bilangan = Bilangan(5)
pangkat = 3

hasil_pangkat = bilangan ** pangkat
print(f"Hasil dari {bilangan.nilai} pangkat {pangkat} adalah: {hasil_pangkat}")
