class Shark:

    def __init__(self, name) -> None:
        self.name = name

    def swim (self):
        print(f'{self.name} is swimming')

    def be_awesome(self):
        print(f'{self.name} is being awesome')

def main():
    sammy = Shark('Sammy')
    sammy.swim()
    sammy.be_awesome()

if __name__ == '__main__':
    main()

