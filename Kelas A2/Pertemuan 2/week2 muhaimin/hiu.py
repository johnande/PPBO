class Shark:
    def __init__(self,name):
         self.name=name
    def swim(self):
        print(self.name + " is swimming.")
    def be_awesome(self):
        print(self.name + "is being awesome.")

def main():
    #set name of shark objek
    sammy= Shark("Sammy")
    sammy.swim()
    sammy.be_awesome()
    
if __name__ == "__main__":
    main()