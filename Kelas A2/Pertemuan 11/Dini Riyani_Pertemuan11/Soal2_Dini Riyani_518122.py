class Model(object):
    services = {
        'email': {'number': 1000, 'price': 2,},
        'sms': {'number': 1000, 'price': 10,},
        'voice': {'number': 1000, 'price': 15,},
    }

class View(object):
    def list_services(self, services, language="English"):
        if language.lower() == "indonesian":
            print("Layanan yang Tersedia:")
        else:
            print("Services Provided:")
        for svc in services:
            print(svc)

    def list_pricing(self, services, language="English"):
        if language.lower() == "indonesian":
            print("Harga Layanan:")
        else:
            print("Pricing for Services:")
        for svc in services:
            if language.lower() == "indonesian":
                print("Untuk", Model.services[svc]['number'],
                      svc, "pesan Anda harus membayar $",
                      Model.services[svc]['price'])
            else:
                print("For", Model.services[svc]['number'],
                      svc, "message you pay $",
                      Model.services[svc]['price'])

class View2(object):
    def list_services(self, services):
        print("Layanan yang Tersedia:")
        for svc in services:
            print(svc)

    def list_pricing(self, services):
        print("Harga Layanan:")
        for svc in services:
            print("Untuk", Model.services[svc]['number'],
                  svc, "pesan Anda harus membayar $",
                  Model.services[svc]['price'])

class Controller(object):
    def __init__(self, language="English"):
        self.model = Model()
        self.view = None  # Akan diinisialisasi setelah bahasa dipilih
        self.language = language

    def select_view(self):
        if self.language.lower() == "indonesian":
            self.view = View2()
        else:
            self.view = View()

    def get_services(self):
        services = self.model.services.keys()
        self.select_view()
        return self.view.list_services(services)

    def get_pricing(self):
        services = self.model.services.keys()
        self.select_view()
        return self.view.list_pricing(services)

# Meminta pengguna memilih bahasa
while True:
    print("Select language / Pilih bahasa:")
    print("1. English")
    print("2. Indonesian")
    language_choice = input("Enter choice (1/2): ")

    if language_choice in ['1', '2']:
        break
    else:
        print("Invalid choice! Please enter '1' for English or '2' for Indonesian.")

# Menetapkan bahasa berdasarkan pilihan pengguna
if language_choice == "2":
    print("Bahasa yang Dipilih: Bahasa Indonesia")
    language_choice = "Indonesian"
else:
    print("Selected Language: English")
    language_choice = "English"

# Membuat instance Controller dengan bahasa yang dipilih
controller = Controller(language=language_choice)
controller.get_services()
controller.get_pricing()
