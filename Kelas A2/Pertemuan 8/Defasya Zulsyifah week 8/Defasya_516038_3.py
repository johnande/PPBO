from abc import ABC, abstractmethod

class Pekerja(ABC):
    def _init_(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji

    @abstractmethod
    def bekerja(self):
        pass

class Programmer(Pekerja):
    def bekerja(self):
        return f"{self.nama} sedang menulis kode."

class Manager(Pekerja):
    def bekerja(self):
        return f"{self.nama} sedang mengelola proyek."

def main():
    programmer = Programmer("Arief", 5000)
    manager = Manager("Budi", 7000)

    pekerjaan = [programmer, manager]

    for pekerja in pekerjaan:
        print(f"{pekerja.nama} bekerja: {pekerja.bekerja()} Gajinya
{pekerja.gaji} dollar.")

if __name__ == "__main__":
    main()