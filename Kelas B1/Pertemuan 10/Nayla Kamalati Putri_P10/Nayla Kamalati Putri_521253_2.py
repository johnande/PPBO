from abc import ABC, abstractmethod

class Section(ABC):
    @abstractmethod
    def describe(self):
        pass

class PersonalSection(Section):
    def describe(self):
        print("Personal Section")

class AlbumSection(Section):
    def describe(self):
        print("Album Section")

class PatentSection(Section):
    def describe(self):
        print("Patent Section")

class PublicationSection(Section):
    def describe(self):
        print("Publication Section")

# Factory class
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

class Linkedin(Profile):
    def create_profile(self):
        self.add_section(PersonalSection())
        self.add_section(PatentSection())
        self.add_section(PublicationSection())

class Facebook(Profile):
    def create_profile(self):
        self.add_section(PersonalSection())
        self.add_section(AlbumSection())

profile_type = input("Profil apa yang ingin anda buat? [Linkedin atau Facebook]: ")
profile = None

if profile_type.lower() == "linkedin":
    profile = Linkedin()
elif profile_type.lower() == "facebook":
    profile = Facebook()
else:
    print("Profil yang diminta tidak tersedia.")

if profile:
    print(f"Profil {type(profile).__name__} sedang dibuat..")
    print("Profil mempunyai Section:")
    for section in profile.get_sections():
        section.describe()
        