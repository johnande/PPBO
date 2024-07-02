class Model(object):
    services = {
        'email': {'number': 1000, 'price': 2,},
        'sms': {'number': 1000, 'price': 10,},
        'voice': {'number': 1000, 'price': 15,},
    }
 
class View(object):
    def list_services(self, services):
        for svc in services:
            print(svc)

    def list_pricing(self, services):
        for svc in services:
            print("For", Model.services[svc]['number'],
                  svc, "message you pay $",
                  Model.services[svc]['price'])

class Controller(object):
    def __init__(self):
        self.menu = input("What language do you choose? [1] English [2] Indonesia:")
        if self.menu == '1':
            self.model = Model()
            self.view = View()
        elif self.menu == '2':
            self.model = Model()
            self.view = View2()
        else:
            print("Error, choose the language number!")
            print("Error, choose the language number!")

    def get_services(self):
        services = self.model.services.keys()
        return self.view.list_services(services)
    
    def get_pricing(self):
        services = self.model.services.keys()
        return self.view.list_pricing(services)

class View2(object):
    def list_services(self, services):
        for svc in services:
            print(svc)

    def list_pricing(self, services):
        for svc in services:
            print("Untuk", Model.services[svc]['number'],
                  svc, "anda membayar $",
                  Model.services[svc]['price'])

#Instansiasi objek
controller = Controller()
if controller.menu == '1':
    print("Services Provided:")
    controller.get_services()
    print("Pricing for Services:")
    controller.get_pricing()
elif controller.menu == '2':
    print("Layanan yang disediakan:")
    controller.get_services()
    print("Tarif tiap layanan:")
    controller.get_pricing()