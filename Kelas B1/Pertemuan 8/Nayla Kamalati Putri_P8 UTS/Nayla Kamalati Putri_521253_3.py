#UTS NO 3
from abc import ABC, abstractmethod

class Smartphone(ABC):
    def __init__(self, merek, model):
        self.merek = merek
        self.model = model

    @abstractmethod
    def tampilkan_info(self):
        pass

class IPhone(Smartphone):
    def __init__(self, model):
        super().__init__("Apple", model)

    def tampilkan_info(self):
        return f"IPhone {self.model}: Ditenagai oleh iOS"

class Android(Smartphone):
    def __init__(self, merek, model):
        super().__init__(merek, model)

    def tampilkan_info(self):
        return f"{self.merek} {self.model}: Ditenagai oleh Android"

def tampilkan_info_smartphone(smartphone):
    print(smartphone.tampilkan_info())

iphone = IPhone("12 Pro Max")
android = Android("Samsung", "Galaxy S21")

print("Informasi tentang Smartphone:")
tampilkan_info_smartphone(iphone)
tampilkan_info_smartphone(android)