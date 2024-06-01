class Model(object):
    services = {
    'email': {'number': 1000, 'price': 2,},
    'sms': {'number': 1000, 'price': 10,},
    'voice': {'number': 1000, 'price': 15,},
    }

class View(object):
    def list_services(self, services):
        for svc in services:
                print(svc,'')
 
    def list_pricing(self, services):
        for svc in services:
            print("For", Model.services[svc]['number'],svc, "message you pay $",Model.services[svc]['price'])

class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View()
 
    def get_services(self):
        services = self.model.services.keys()
        return(self.view.list_services(services))
 
    def get_pricing(self):
        services = self.model.services.keys()
        return(self.view.list_pricing(services))

    def bid_price(self):
        tawar = input("what service do you want to bid? email, sms, voice: ")
        if tawar not in self.model.services.keys():
            print("Service not available")
        else:
            print(f"Current price for {tawar} service: ${self.model.services[tawar]['price']}")
            harga = int(input("how much do you want to bid? (in $): "))
            self.model.services[tawar]['price'] = harga
            print(f"Price according to your bid:")
            self.get_pricing()

controller = Controller()
print("Services Provided:")
controller.get_services()
print("Pricing for Services:")
controller.get_pricing()

bid = input("Do you want to bid the price? [y/n]: ")
if bid == 'y':
    controller.bid_price()
elif bid == 'n':
    print("Thank you for using our service")
else:
    print("Invalid input")


