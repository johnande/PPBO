from abc import ABC, abstractmethod

class Timezone(ABC):
    def __init__(self, nama, koin):
        self.nama = nama
        self.koin = koin
    @abstractmethod
    def harga(self):
        pass

class Maimai(Timezone):
    def harga(self):
        biaya = 2000
        if self.koin >= biaya:
            sisa_koin = self.koin - biaya
            print(f"{self.nama} harga per main {biaya}")
            print(f"Sisa koin {sisa_koin}")
            return sisa_koin
        else:
            print("Koin yang dimiliki kurang")
            return 0

class Snapshot(Timezone):
    def harga(self):
        biaya = 25000    
        if self.koin >= biaya:
            sisa_koin = self.koin - biaya
            print(f"{self.nama} harga per main {biaya}")
            print(f"Sisa koin {sisa_koin}")
            return sisa_koin
        else:
            print("Koin yang dimiliki kurang")
            return 0

koin_awal = 50000
print(f"Koin awal: {koin_awal}")

main1 = Maimai("Maimai", koin_awal)
sisa_koin_main1 = main1.harga()

main2 = Snapshot("Snapshot", sisa_koin_main1)
sisa_koin_main2 = main2.harga()

main3 = Maimai("Maimai", sisa_koin_main2)
sisa_koin_main3 = main3.harga()

main4 = Snapshot("Snapshot", sisa_koin_main3)
sisa_koin_main4 = main4.harga()

