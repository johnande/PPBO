class Model(object):
    services = {
        'email': {'number': 1000, 'price': 2,},
        'sms': {'number': 1000, 'price': 10,},
        'voice': {'number': 1000, 'price': 15,},
    }
class View(object):
    def select_language(self):
        lang_choice = input("What language do you choose?:" "[1] English" "[2] Indonesia: ")
        return lang_choice
    def list_services(self, services, lang):
        if lang == '1':  # English
            for svc in services:
                print(svc, '')
        elif lang == '2':  # Bahasa Indonesia
            for svc in services:
                print(svc, '')
    def list_pricing(self, services, lang):
        if lang == '1':  # English
            for svc in services:
                print("For", Model.services[svc]['number'],
                      svc, "message you pay $",
                      Model.services[svc]['price'])
        elif lang == '2':  # Bahasa Indonesia
            for svc in services:
                print("Untuk", Model.services[svc]['number'],
                      "pesan", svc, "Anda membayar $",
                      Model.services[svc]['price'])
class View2(object):  # New View for Indonesian language
    def select_language(self):
        lang_choice = input("Bahasa apa yang Anda pilih?:" "[1] Inggris" "[2] Indonesia: ")
        return lang_choice
    def list_services(self, services, lang):
        if lang == '1':  # English
            for svc in services:
                print(svc, '')
        elif lang == '2':  # Bahasa Indonesia
            for svc in services:
                print(svc, '')
    def list_pricing(self, services, lang):
        if lang == '1':  # English
            for svc in services:
                print("For", Model.services[svc]['number'],
                      svc, "message you pay $",
                      Model.services[svc]['price'])
        elif lang == '2':  # Bahasa Indonesia
            for svc in services:
                print("Untuk", Model.services[svc]['number'],
                      "pesan", svc, "Anda membayar $",
                      Model.services[svc]['price'])
class Controller(object):
    def __init__(self):
        self.model = Model()
        self.language_choice = ''
    def set_language(self):
        self.language_choice = input("What language do you choose?:" "[1] English" "[2] Indonesia: ")
        if self.language_choice == '1':
            self.view = View()
        elif self.language_choice == '2':
            self.view = View2()
        else:
            print("Error, choose the language number!")
            print("Error, choose the language number!")
            exit()
    def get_services(self):
        services = self.model.services.keys()
        return self.view.list_services(services, self.language_choice)

    def get_pricing(self):
        services = self.model.services.keys()
        return self.view.list_pricing(services, self.language_choice)
controller = Controller()
controller.set_language()
if controller.language_choice == '1':
    print("Services Provided:")
    controller.get_services()
    print("Pricing for Services:")
    controller.get_pricing()
elif controller.language_choice == '2':
    print("Layanan yang disediakan:")
    controller.get_services()
    print("Harga untuk Layanan:")
    controller.get_pricing()