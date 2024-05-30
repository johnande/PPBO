class Kendaraan:
    def __init__(self, merek, jenis):
        self.merek = merek
        self.jenis = jenis
    
    def ngeprint(self):
        print(f"Merk kendaraan adalah {self.merek} dan jenis kendaraan adalah {self.jenis}.")

# Membuat objek mobil
mobil = Kendaraan("Toyota", "Innova")
mobil.ngeprint()

# Membuat objek motor
motor = Kendaraan("Honda", "Revo")
motor.ngeprint()