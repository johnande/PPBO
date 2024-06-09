class Mobil:
    def merek(self):
        pass

class nissan(Mobil):
    def merek(self):
        return "broom!!!"
    
class toyota(Mobil):
    def merek(self):
        return "vroomm!"
    
def Mobil_Sound(mobil):
    return mobil.merek()

R34 = nissan()
Supra = toyota()

print(Mobil_Sound(R34))
print(Mobil_Sound(Supra))
    
