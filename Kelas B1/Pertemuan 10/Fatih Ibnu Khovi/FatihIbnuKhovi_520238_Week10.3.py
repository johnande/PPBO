from abc import ABC, abstractmethod

class Section(ABC):
    @abstractmethod
    def describe(self):
        pass

class SneakerSection(Section):
    def describe(self):
        print("Sneaker Section")

class BootSection(Section):
    def describe(self):
        print("Boot Section")

class SandalSection(Section):
    def describe(self):
        print("Sandal Section")

class Profile(ABC):
    def __init__(self):
        self.sections = []
        self.create_profile()
    
    @abstractmethod
    def create_profile(self):
        pass
    
    def get_sections(self):
        return self.sections
    
    def add_section(self, section):
        self.sections.append(section)
        
class AdidasProfile(Profile):
    def create_profile(self):
        self.add_section(SneakerSection())
        self.add_section(BootSection())

class NikeProfile(Profile):
    def create_profile(self):
        self.add_section(SneakerSection())
        self.add_section(SandalSection())

profile_type = input("Apa jenis profil sepatu yang ingin Anda buat? [Adidas atau Nike]: ")
profile = eval(profile_type.capitalize() + "Profile")()
print(f"Profil {type(profile).__name__} sedang dibuat..")
print("Profil memiliki Section:")
for section in profile.get_sections():
    section.describe()