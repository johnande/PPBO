from abc import ABC, abstractmethod

class KeberagamanIndonesia(ABC):
    @abstractmethod
    def tarian(self):
        pass
    
    @abstractmethod
    def rumah_adat(self):
        pass

class JawaTengah(KeberagamanIndonesia):
    name = "Jawa Tengah"
    def tarian(self):
        return "Kuda Lumping"
    
    def rumah_adat(self):
        return "Rumah Joglo"

class JawaBarat(KeberagamanIndonesia):
    name = "Jawa Barat"
    def tarian(self):
        return "Jaipong"
    
    def rumah_adat(self):
        return "Rumah Panggung"

class JawaTimur(KeberagamanIndonesia):
    name = "Jawa Timur"
    def tarian(self):
        return "Tari Reog Ponorogo"
    
    def rumah_adat(self):
        return "Rumah Joglo"

jateng = JawaTengah()
jabar = JawaBarat()
jatim = JawaTimur()

for i in (jateng, jabar, jatim):
    print("Tarian adat dari", i.name, ":", i.tarian())
    print("Rumah adat dari", i.name, ":", i.rumah_adat())
    print()