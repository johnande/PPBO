from abc import ABC, abstractmethod

# Abstract class for computer components
class Component(ABC):
    @abstractmethod
    def specification(self):
        pass

# Concrete components
class CPU(Component):
    def specification(self):
        return "Quad-core Intel Core i7"

class RAM(Component):
    def specification(self):
        return "16GB DDR4"

class GPU(Component):
    def specification(self):
        return "NVIDIA GeForce RTX 3080"

# Abstract factory class
class ComputerFactory(ABC):
    @abstractmethod
    def create_cpu(self):
        pass
    
    @abstractmethod
    def create_ram(self):
        pass
    
    @abstractmethod
    def create_gpu(self):
        pass

# Concrete factory classes
class GamingComputerFactory(ComputerFactory):
    def create_cpu(self):
        return CPU()
    
    def create_ram(self):
        return RAM()
    
    def create_gpu(self):
        return GPU()

class OfficeComputerFactory(ComputerFactory):
    def create_cpu(self):
        return CPU()
    
    def create_ram(self):
        return RAM()
    
    def create_gpu(self):
        return None  # Office computers may not have a dedicated GPU

# Client code
def main():
    # Asking user for computer type
    computer_type = input("What type of computer do you want? [Gaming or Office]: ").lower()

    # Creating factory based on user's choice
    if computer_type == "gaming":
        factory = GamingComputerFactory()
    elif computer_type == "office":
        factory = OfficeComputerFactory()
    else:
        print("Invalid computer type!")
        return

    # Building the computer
    cpu = factory.create_cpu()
    ram = factory.create_ram()
    gpu = factory.create_gpu()

    # Displaying computer components
    print("Computer components:")
    print("CPU:", cpu.specification())
    print("RAM:", ram.specification())
    if gpu:
        print("GPU:", gpu.specification())
    else:
        print("GPU: Integrated graphics")

if __name__ == "__main__":
    main()
