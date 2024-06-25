class Converter:
    def konversi(self, suhu):
        pass

class Celsius(Converter):
    def konversi(self, suhu):
        return (suhu * 9/5) + 32

class Fahrenheit(Converter):
    def konversi(self, suhu):
        return (suhu - 32) * 5/9

class Factory:
    @staticmethod
    def buat_converter(jenis_konversi):
        if jenis_konversi == "Celsius ke Fahrenheit":
            return Celsius()
        elif jenis_konversi == "Fahrenheit ke Celsius":
            return Fahrenheit()
        else:
            raise ValueError("Jenis konversi tidak valid")

# Penggunaan Factory Pattern
konverter1 = Factory.buat_converter("Celsius ke Fahrenheit")
print("29 derajat Celsius setara dengan", konverter1.konversi(29), "F")
konverter2 = Factory.buat_converter("Fahrenheit ke Celsius")
print("90 derajat Fahrenheit setara dengan", konverter2.konversi(90), "C")
