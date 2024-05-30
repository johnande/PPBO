#parent class
class bird:
    def __init__(self):
        print("Bird is ready")
    
    def whoisthis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")


#child class
class penguin(bird):
    def __init__(self):
        #call super() function
        super().__init__()
        print("Penguin is ready")
    
    def whoisthis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

#https://pbs.twimg.com/media/GGSJlZeawAAPDeI?format=jpg&name=large
topan = penguin()
topan.whoisthis()
topan.swim()
topan.run()