class Model(object):
    services = {
        'email': {'number': 1000, 'price': 2,},
        'sms': {'number': 1000, 'price': 10,},
        'voice': {'number': 1000, 'price': 15,},
    }
class View(object):
    def list_services(self, services):
        for svc in services:
            print(svc, '')
    def list_pricing(self, services):
        for svc in services:
            print("For", Model.services[svc]['number'],
                  svc, "message you pay $",
                  Model.services[svc]['price'])     
class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View()
    def get_services(self):
        services = self.model.services.keys()
        return self.view.list_services(services)
    def get_pricing(self):
        services = self.model.services.keys()
        return self.view.list_pricing(services)
    def bid_price(self):
        tawar = input("Enter the service you want to bid on (email, sms, voice): ")
        if tawar not in self.model.services:
            print("Service not found.")
            return
        try:
            harga = float(input(f"Enter your bid price for {tawar}: "))
            if harga < 0:
                raise ValueError("Price cannot be negative.")
        except ValueError as e:
            print(f"Invalid input: {e}")
            return
        self.model.services[tawar]['price'] = harga
        print("Price according to your bid")
        self.get_pricing()
controller = Controller()
print("Services Provided:")
controller.get_services()
print("Pricing for Services:")
controller.get_pricing()
controller.bid_price()
