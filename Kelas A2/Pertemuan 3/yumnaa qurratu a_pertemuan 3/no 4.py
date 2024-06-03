# parent class
class Bird:
    
    def __init__(self):
        print("Bird is ready")
        
    def whoisThis(self):
        print("Bird")
        
    def swim(self):
        print("Swim faster")
        
# child class
class penguin(Bird):
    
    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")
        
    def whoisThis(self):
        print("Penguin")
        
    def run(self):
        print("Run faster")
        
peggy = penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()

