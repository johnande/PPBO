class Person:
    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def fullname(self): # instance method
        return "%s %s" % (self.name, self.surname) # instance object accessible through self

    @property
    def fullname2(self):
        return "%s %s" % (self.name, self.surname)

    @classmethod
    def allowed_titles_starting_with(cls, startswith): # class method
        return [t for t in cls.TITLES if t.startswith(startswith)]  # class or instance object accessible through cls

    @staticmethod
    def allowed_titles_ending_with(endswith): 
        return [t for t in Person.TITLES if t.endswith(endswith)] # no parameter for class or instance object & we have to use Person directly

jane = Person("Jane", "Smith")

print(jane.fullname())
print(jane.fullname2) # no brackets!
print(jane.allowed_titles_starting_with("M"))
print(Person.allowed_titles_starting_with("M"))
print(jane.allowed_titles_ending_with("s"))
print(Person.allowed_titles_ending_with("s"))