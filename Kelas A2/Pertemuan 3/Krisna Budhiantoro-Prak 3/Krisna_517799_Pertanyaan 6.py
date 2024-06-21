# kelas induk
class Bird:

    def __init__(self):
        print("Burung siap")

    def whoisThis(self):
        print("Burung")

    def swim(self):
        print("Berenang lebih cepat")

class Penguin(Bird):

    def __init__(self):        # panggil fungsi super()
        super().__init__()
        print("Penguin siap")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Berlari lebih cepat")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
