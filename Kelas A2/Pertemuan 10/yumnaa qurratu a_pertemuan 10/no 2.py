from abc import ABC, abstractmethod

class Section(ABC):
    @abstractmethod
    def describe(self):
        pass

class PersonalSection(Section):
    def describe(self):
        return "Personal Section"

class AlbumSection(Section):
    def describe(self):
        return "Album Section"

class PatentSection(Section):
    def describe(self):
        return "Patent Section"

class PublicationSection(Section):
    def describe(self):
        return "Publication Section"

#Factory class
class Profile(ABC):
    def __init__(self):
        self.sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self.sections
 
    def addSections(self, section):
        self.sections.append(section)

class Linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PatentSection())
        self.addSections(PublicationSection())

class Facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())

profile_type = input("Profil apa yang ingin anda buat? [Linkedin atau Facebook]: ")
if profile_type.lower() == "linkedin":
    profile = Linkedin()
elif profile_type.lower() == "facebook":
    profile = Facebook()
else:
    print("Profil tidak ditemukan")
    exit()

print(f"Profil {type(profile).__name__} sedang dibuat..")
print("Profil mempunyai Section:")
for section in profile.getSections():
    print(section.describe())

