class person (object):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
    def is_employee(self):
        return False
    
class employee(person):
    def is_employee(self):
        return True
    
emp = person("slamet")
print(emp.get_name(), emp.is_employee())

