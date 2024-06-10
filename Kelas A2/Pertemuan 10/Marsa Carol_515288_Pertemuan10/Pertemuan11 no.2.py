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

class View2(object):
    def list_services(self, services):
        for svc in services:
            print(svc, '')

    def list_pricing(self, services):
        for svc in services:
            print("Untuk", Model.services[svc]['number'],
                svc, "pesan Anda harus membayar $",
                Model.services[svc]['price'])

class Controller(object):
    def __init__(self):
        language_choice = input("What language do you choose? [1] English, [2] Indonesia: ")
        while language_choice not in ['1', '2']:
            print("Error! Choose the language number!")
            language_choice = input("What language do you choose? [1] English, [2] Indonesia: ")

        if language_choice == '1':
            self.view = View()
            self.service_message = "Services Provided:"
            self.pricing_message = "Pricing for Services:"
        elif language_choice == '2':
            self.view = View2()
            self.service_message = "Layanan yang Tersedia:"
            self.pricing_message = "Tarif tiap layanan:"

    def get_services(self):
        services = Model.services.keys()
        print(self.service_message)
        return self.view.list_services(services)

    def get_pricing(self):
        services = Model.services.keys()
        print(self.pricing_message)
        return self.view.list_pricing(services)

# Instansiasi objek
controller = Controller()
controller.get_services()
controller.get_pricing()