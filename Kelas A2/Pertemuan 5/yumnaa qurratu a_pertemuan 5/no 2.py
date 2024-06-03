class Ikan:
    def perkenalan(self):
        print("Ada banyak jenis ikan.")

    def berenang(self):
        print("Sebagian besar ikan bernafas menggunakan ingsang, tetapi ada yang tidak.")

class IkanMujahir(Ikan):
    def berenang(self):
        print("Ikan mujahir bernafas menggunakan ingsang.")

class IkanPaus(Ikan):
    def berenang(self):
        print("Ikan Paus tidak bernafas menggunakan ingsang.")

obj_ikan = Ikan()
obj_ikan_mujahir = IkanMujahir()
obj_ikan_paus = IkanPaus()

obj_ikan.perkenalan()
obj_ikan.berenang()

obj_ikan_mujahir.perkenalan()
obj_ikan_mujahir.berenang()

obj_ikan_paus.perkenalan()
obj_ikan_paus.berenang()

