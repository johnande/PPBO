class Model(object):
    services = {
    'email': {'number': 1000, 'price': 2,},
    'sms': {'number': 1000, 'price': 10,},
    'voice': {'number': 1000, 'price': 15,},
    }

class View(object):
    def list_services(self, services):
        print("Services Provided:")
        for svc in services:
            print(svc,'')
    def list_pricing(self, services):
        print("Pricing for Services:")
        for svc in services:
            print("For", Model.services[svc]['number'],
                svc, "message you pay $",
                Model.services[svc]['price'])

class View2(object):
    def list_services(self, services):
        print("Layanan yang disediakan:")
        for svc in services:
            print(svc,'')
    def list_pricing(self, services):
        print("Tarif tiap layanan:")
        for svc in services:
            print("Untuk setiap", Model.services[svc]['number'],
                svc, "anda membayar $",
                Model.services[svc]['price'])

class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View()
        while True:
            self.bahasa = input("What language do you choose? [1]English [2]Indonesia: ")
            if self.bahasa == "1":
                self.view = View()
                break
            elif self.bahasa == "2":
                self.view = View2()
                break
            else:
                print("Error, choose the language number!")
    def get_services(self):
        services = self.model.services.keys()
        return(self.view.list_services(services))
    def get_pricing(self):
        services = self.model.services.keys()
        return(self.view.list_pricing(services))
    def bid_price(self):
        while True:
            tawar = input("What service do you want to bid? email, sms, or voice: ") if self.bahasa == "1" else input("Layanan apa yang ingin Anda tawar? email, sms, atau voice: ")
            if tawar in ["email", "sms", "voice"]:
                break
            else:
                print("Invalid service. Please input a valid service!" if self.bahasa == "1" else "Layanan tidak valid. Mohon masukkan layanan yang valid!")
        harga = int(input("Enter the price you want (in $): ")) if self.bahasa == "1" else int(input("Masukkan harga yang Anda inginkan (dalam $): "))
        self.model.services[tawar] = {'number': 1000, 'price': harga}
        print("Price according to your bid:" if self.bahasa == "1" else "Harga sesuai dengan tawaran Anda:")
        self.get_pricing()

#Instansiasi objek
controller = Controller()
controller.get_services()
controller.get_pricing()
controller.bid_price()