#================================================================ Soal nomor 1
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
            print("For", Model.services[svc]['number'],
                svc, "message you pay $",
                Model.services[svc]['price'])
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

#Instansiasi objek
controller = Controller()
print("Services Provided:")
controller.get_services()
print("Pricing for Services:")
controller.get_pricing()

#============================================================== Soal nomor 2
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
                  svc, "messages you pay $",
                  Model.services[svc]['price'])

class View2(object):
    def list_services(self, services):
        for svc in services:
            print(svc, '')
    
    def list_pricing(self, services):
        for svc in services:
            print("Untuk", Model.services[svc]['number'],
                  svc, "anda membayar $",
                  Model.services[svc]['price'])

class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View()
    
    def choose_languages(self):
        language_choice = input("What language do you choose? \n[1] English\n[2] Indonesia\n\nAnswer: ")
        if language_choice == "1":
            self.view = View()
            return True
        elif language_choice == "2":
            self.view = View2()
            return False
        else:
            print("\nError, choose the language number!")
            return False
    
    def get_services(self):
        services = self.model.services.keys()
        return self.view.list_services(services)
    
    def get_pricing(self):
        services = self.model.services.keys()
        return self.view.list_pricing(services)

# Instansiasi objek
controller = Controller()
if controller.choose_languages():
    print("Services Provided:")
    controller.get_services()
    print("Pricing for Services:")
    controller.get_pricing()
elif controller.choose_languages():
    controller.view = View2()  # Switch to View2 in case of invalid language choice or choosing Indonesian
    print("Layanan yang disediakan:")
    controller.get_services()
    print("Tarif tiap layanan:")
    controller.get_pricing()
else:
    print("Error, choose the language number!")


#============================================================== Soal nomor 3
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
                  svc, "messages you pay $",
                  Model.services[svc]['price'])

class View2(object):
    def list_services(self, services):
        for svc in services:
            print(svc, '')
    def list_pricing(self, services):
        for svc in services:
            print("Untuk", Model.services[svc]['number'],
                  svc, "anda membayar $",
                  Model.services[svc]['price'])

class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View()
    
    def choose_languages(self):
        language_choice = input("What language do you choose? \n [1] English\n [2] Indonesia\n\nAnswer: ")
        if language_choice == "1":
            self.view = View()
        elif language_choice == "2":
            self.view = View2()
        else:
            print("\nError: choose the language number!")
            return False
        return True
    
    def get_services(self):
        services = self.model.services.keys()
        return self.view.list_services(services)
    
    def get_pricing(self):
        services = self.model.services.keys()
        return self.view.list_pricing(services)
    
    def bid_price(self):
        # Meminta input dari user untuk jenis layanan dan harga penawaran
        tawar = input("\nWhat service do you want to bid? email, sms, or voice: ").strip().lower()
        if tawar not in self.model.services:
            print("Error: service not available!")
            return
        try:
            harga = float(input("Enter the price you want (in $): "))
        except ValueError:
            print("Error, invalid price entered!")
            return
        
        # Update dictionary services dengan harga baru
        self.model.services[tawar]['price'] = harga
        
        # Tampilkan string “Price according to your bid”
        print("Price according to your bid")
        
        # Panggil method get_pricing
        self.get_pricing()

controller = Controller()
if controller.choose_languages():
    print("Services Provided:" if isinstance(controller.view, View) else "Layanan yang disediakan:")
    controller.get_services()
    print("Pricing for Services:" if isinstance(controller.view, View) else "Tarif tiap layanan:")
    controller.get_pricing()
    controller.bid_price()
