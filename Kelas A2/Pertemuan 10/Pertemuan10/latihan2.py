from abc import ABC, abstractmethod

class section(ABC):
    @abstractmethod
    def describe(self):
        pass

class personalsection(section):
    def describe(self):
        print('Personal Section')

class albumsection(section):
    def describe(self):
        print('Album Section')

class patentsection(section):
    def describe(self):
        print('Patent Section')

class publicationsection(section):
    def describe(self):
        print('Publication Section')

# factory class
class profile(ABC):
    def __init__(self):
        self.sections = []
        self.createprofile()
    
    @abstractmethod 
    def createprofile(self):
        pass
    
    def getsections(self):
        return self.sections
    
    def addsection(self, section):
        self.sections.append(section)

class linkedin(profile):
    def createprofile(self):
        self.addsection(personalsection())
        self.addsection(patentsection())
        self.addsection(publicationsection())   

class facebook(profile):    
    def createprofile(self):
        self.addsection(personalsection())
        self.addsection(albumsection())
        
profiletype = input("Which profile would you like to create? [LinkedIn/Facebook] ")
profile = eval(profiletype.lower())()
print(f"creating {type(profile).__name__} profile...")
for section in profile.getsections():
    print(section.describe())