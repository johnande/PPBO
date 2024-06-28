class TemperatureConverter:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        return cls((fahrenheit - 32) * 5/9)

    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15


# Membuat objek
temperature = TemperatureConverter(25)

# Menggunakan property
print("Temperature in Celsius:", temperature.celsius)
print("Temperature in Fahrenheit:", temperature.fahrenheit)

# Menggunakan class method
temperature2 = TemperatureConverter.from_fahrenheit(77)
print("Temperature in Celsius (from Fahrenheit):", temperature2.celsius)

# Menggunakan static method
print("300 Kelvin in Celsius:", TemperatureConverter.kelvin_to_celsius(300))
