class Shark:
    def __init__(self, name):
        self.name = name

    def swim(self):
        print(self.name + " is swiming.")

    def be_awesome(self):
        print(self.name + " is being awasome.")


def main():
    sammy = Shark("Sammy")
    sammy.swim()
    sammy.be_awesome()


if __name__ == "__main__":
    main()