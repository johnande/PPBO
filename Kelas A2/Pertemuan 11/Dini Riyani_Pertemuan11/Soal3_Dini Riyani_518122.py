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
        tawar = input("Enter the type of service to bid on (email/sms/voice): ")
        if tawar in Model.services:
            price = float(input("Enter the bidding price: "))
            self.model.services[tawar] = {'number': 1000, 'price': price}
            print("Price according to your bid:")
            self.get_pricing()
        else:
            print("Invalid service type. Please enter email, sms, or voice.")

# Instantiate the object
controller = Controller()
print("Services Provided:")
controller.get_services()
print("Pricing for Services:")
controller.get_pricing()
controller.bid_price()
