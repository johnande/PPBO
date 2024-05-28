class person:
    sehat = False
    
    def dinyatakan_sehat(self):
        self.sehat = True
        
joni= person()
eko= person()

joni.dinyatakan_sehat()
print("joni sehat:", joni.sehat) # nilai terbarui
print("Eko sehat:", eko.sehat)  # nilai default
