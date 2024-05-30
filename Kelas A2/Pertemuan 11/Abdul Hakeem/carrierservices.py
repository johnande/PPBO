# mvc pattern implementation

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

class carriercontroller(object):
    def __init__(self):
        self.model = carriermodel()
        self.view = carrierview_en_US()

    def getservices(self):
        services = self.model.services.keys()
        return(self.view.listservices(services))
    
    def getpricing(self):
        services = self.model.services.keys()
        return(self.view.listpricing(services))
    
# instantiate object
controller = carriercontroller()
print("Services Provided:")
controller.getservices()
print("Pricing:")
controller.getpricing()