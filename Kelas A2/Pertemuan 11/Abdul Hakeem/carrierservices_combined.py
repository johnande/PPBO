import sys # contingency plan
class carriermodel(object):
    services = {
        'email' : {'number' : 1000, 'price' : 2,},
        'sms' : {'number' : 1000, 'price' : 10,},
        'voice' : {'number' : 1000, 'price' : 15,} , 
    }

class carrierview_en_US(object):
    def listservices(self, services):
        for service in services:
            print(service, '')

    def listpricing(self, services):
        for service in services:
            print(f"for {carriermodel.services[service]['number']} {service} messages, you pay ${carriermodel.services[service]['price']}")

class carrierview_id_ID(object):
    def listservices(self, services):
        for service in services:
            print(service, '')

    def listpricing(self, services):
        for service in services:
            print(f"untuk {carriermodel.services[service]['number']} pesan {service}, Anda membayar Rp{carriermodel.services[service]['price']*16000}")

class carriercontroller(object):
    def __init__(self, locale):
        self.model = carriermodel()
        self.locale = locale
        if locale == 'en_US':
            self.view = carrierview_en_US()
        elif locale == 'id_ID':
            self.view = carrierview_id_ID()
        else:
            print("how are you here? contact the dev with repro steps")
            exit()

    def getservices(self):
        services = self.model.services.keys()
        return(self.view.listservices(services))
    
    def getpricing(self):
        services = self.model.services.keys()
        return(self.view.listpricing(services))
    
    def bidprice(self, service, price):
        carriermodel.services[service]['price'] = price
    
# instantiate object, an thread #

# langcheck
print("""Pilihan Bahasa:
      1. English (en_US)
      2. Bahasa Indonesia (id_ID)""")
try:
    lang = int(input("Masukkan kode bahasa (1, 2): "))
except ValueError:
    print("Please input a number.")
    exit()
if lang == 1:
    controller = carriercontroller("en_US")
elif lang == 2:
    controller = carriercontroller("id_ID")
else:
    print("Please input a valid number.")
    exit()
        
#output
if controller.locale == "en_US":
    print("Services Provided:")
    controller.getservices()
    print("Pricing:")
    controller.getpricing()
    print("Bidding:")
    print("Which service do you want to bid?")
    service = input()
    if service not in carriermodel.services.keys():
        print("Service not found.")
        exit()
    print("What is your bid price?")
    try:
        price = float(input())
    except ValueError:
        print("Please input a number.")
        exit()
    controller.bidprice(service, price)
    print("New Pricing after bid:")
    controller.getpricing()
elif controller.locale == 'id_ID':
    print("Layanan yang Disediakan:")
    controller.getservices()
    print("Harga:")
    controller.getpricing()
    print("Tawar:")
    print("Layanan mana yang ingin Anda tawar?")
    service = input()
    if service not in carriermodel.services.keys():
        print("Layanan tidak ditemukan.")
        exit()
    print("Berapa harga tawaran Anda?")
    try:
        price = float(input())
    except ValueError:
        print("Silakan masukkan angka.")
        exit()
    controller.bidprice(service, price)
    print("Harga Baru setelah Penawaran:")
    controller.getpricing()
else:
    print("how are you here? contact the dev with repro steps")
    sys.cls()
    exit()







