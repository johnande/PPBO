class person:
    titles = ('Dr', 'Mr', 'Mrs', 'Ms')

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def fullname(self):
        return "%s %s" % (self.name, self.surname) 
    
    @property
    def fullname2(self):
        return "%s %s" % (self.name, self.surname)
    
    @classmethod
    def allowed_titles_starting_with(cls, startswith):
        return [t for t in cls.titles if t.startswith(startswith)]
    
    @staticmethod
    def allowed_titles_ending_with(endswith):
        return [t for t in person.titles if t.endswith(endswith)]
    


jane = person("Jane", "Smith")

print(jane.fullname())  
print(jane.fullname2)

print(jane.allowed_titles_starting_with("M"))
print(person.allowed_titles_ending_with("M"))

print(jane.allowed_titles_starting_with("s"))
print(person.allowed_titles_ending_with("s"))