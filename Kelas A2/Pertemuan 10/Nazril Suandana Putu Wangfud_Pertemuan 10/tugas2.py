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
            print(svc)

    def list_pricing(self, services):
        print("Pricing for sevices :")
        for svc in services:
            print("For", Model.services[svc]['number'],
                svc, "message you pay $",
                Model.services[svc]['price'])

class View2(object):
    def list_services(self, services):
        print("Layanan yang disediakan:")
        for svc in services:
            print(svc)

    def list_pricing(self, services):
        print("Tarif tiap layanan:")
        for svc in services:
            print("Untuk", Model.services[svc]['number'],
                svc, "pesan anda bayar $",
                Model.services[svc]['price'])

class Controller(object):
    def __init__(self, language):
        if language == '1':
            self.view = View()
            self.model = Model()
        elif language == '2':
            self.view = View2()
            self.model = Model()
        else:
            self.view = View()
            self.model = Model()
            print("Error, Choose the language number!")

    def get_services(self):
        services = self.model.services.keys()
        return(self.view.list_services(services))

    def get_pricing(self):
        services = self.model.services.keys()
        return(self.view.list_pricing(services))

# Instansiasi objek
language = input("what language do you choose? [1]English [2]Indonesia :")
if language not in ['1', '2']:
    print("Error, Choose the language number!")
    print("Error, Choose the language number!")
else:
    controller = Controller(language)
    controller.get_services()
    controller.get_pricing()