class Bird:
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Pinguin is ready")

    def whoisThis(self):
        print("Pinguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run