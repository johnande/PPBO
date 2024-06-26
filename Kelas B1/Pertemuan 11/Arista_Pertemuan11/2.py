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
            print("For", Model.services[svc]['number'], svc, "message you pay $", Model.services[svc]['price'])

class View2(object):
    def list_services(self, services):
        for svc in services:
            print(svc)

    def list_pricing(self, services):
        for svc in services:
            print("Untuk setiap", Model.services[svc]['number'], svc, "anda membayar $", Model.services[svc]['price'])

class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view_en = View()
        self.view_id = View2()

    def get_services(self, lang):
        services = self.model.services.keys()
        if lang.lower() == '1' or lang.lower() == 'english':
            return self.view_en.list_services(services)
        elif lang.lower() == '2' or lang.lower() == 'indonesia':
            return self.view_id.list_services(services)
        else:
            print("Error, choose the language number!")

    def get_pricing(self, lang):
        services = self.model.services.keys()
        if lang.lower() == '1' or lang.lower() == 'english':
            return self.view_en.list_pricing(services)
        elif lang.lower() == '2' or lang.lower() == 'indonesia':
            return self.view_id.list_pricing(services)
        else:
            print("Error, choose the language number!")

# Instansiasi objek
controller = Controller()

language_choice = input("What language do you choose? [1] English [2] Indonesia: ")

if language_choice.lower() == '1' or language_choice.lower() == 'english':
    print("Services Provided:")
    controller.get_services('English')
    print("Pricing for Services:")
    controller.get_pricing('English')
elif language_choice.lower() == '2' or language_choice.lower() == 'indonesia':
    print("Layanan yang disediakan:")
    controller.get_services('Indonesia')
    print("Tarif tiap layanan:")
    controller.get_pricing('Indonesia')
else:
    print("Error, choose the language number!")
