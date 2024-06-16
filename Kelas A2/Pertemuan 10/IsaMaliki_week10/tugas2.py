class Model(object):
    services = {
        'email': {'number': 1000, 'price':2,},
        'sms': {'number': 1000, 'price': 10,},
        'voice': {'number': 1000, 'price': 15,},
    }

class View(object):
    def list_services(self, services):
        print("Services Provided:")
        for svc in services:
            print(svc, '')

    def list_pricing(self, services):
        print("Pricing for services:")
        for svc in services:
            print("For", Model.services[svc]['number'],
                  svc, "message you pay $",
                  Model.services[svc]['price'])
            
class View2(object):
    def list_services(self, services):
        print("Layanan yang disediakan:")
        for svc in services:
            print(svc, '')

    def list_pricing(self, services):
        print("Tarif tiap layanan:")
        for svc in services:
            print("Untuk setiap", Model.services[svc]['number'],
                  svc, "anda membayar $",
                  Model.services[svc]['price'])
            
class Controller(object):
    def __init__(self,lang):
        self.model = Model()
        self.lang = lang
        if self.lang == '1':
            self.view = View()
        elif self.lang == '2':
            self.view = View2()

    def get_services(self):
        services = self.model.services.keys()
        return(self.view.list_services(services))
    
    def get_pricing(self):
        services = self.model.services.keys()
        return(self.view.list_pricing(services))
    
if __name__ == '__main__':
    try:
        language = input("What language do you choose? [1]English [2]Indonesia: ")
        controller = Controller(language)
        controller.get_services()
        controller.get_pricing()
    except:
        print("Error, choose the language number!")
        print("Error, choose the language number!")