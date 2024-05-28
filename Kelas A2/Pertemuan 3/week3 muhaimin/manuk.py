# parent class
class Bird:
    def __init__(self):
        print("Manuk is Ready")
        
    def whoisthis(self):
        print("Manuk")
    
    def swim(self):
        print("Swim faster")
# child class
class penguin(Bird):
    def __init__(self):
        super().__init__()
        print("penguin is ready")
    def whoisthis(self):
        print("penguin")
    def run(self):
        print("Run faster")

peggy=penguin()
peggy.whoisthis()
peggy.swim()
peggy.run()