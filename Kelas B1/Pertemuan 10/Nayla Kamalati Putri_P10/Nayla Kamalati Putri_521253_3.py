class Minuman:
    def kemasan(self):
        pass

class Kopi(Minuman):
    def kemasan(self):
        return "Kopi dikemas dalam kemasan kertas"

class Teh(Minuman):
    def kemasan(self):
        return "Teh dikemas dalam kemasan celup"

class FactoryMinuman:
    @staticmethod
    def buat_minuman(jenis_minuman):
        if jenis_minuman == "Kopi":
            return Kopi()
        elif jenis_minuman == "Teh":
            return Teh()
        else:
            raise ValueError("Minuman ini belum tersedia")

factory_minuman = FactoryMinuman()

kopi = factory_minuman.buat_minuman("Kopi")
teh = factory_minuman.buat_minuman("Teh")

print(kopi.kemasan()) 
print(teh.kemasan())  
