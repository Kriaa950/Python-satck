# Create a Pet class with the pet attributes listed above
class Pet:
    def __init__(self, name, type, tricks, health=100, energy=100):
        self.name = name 
        self.type = type 
        self.tricks = tricks
        self.health = health
        self.energy = energy
    def sleep(self):
        print(f"{self.name} is sleeping.")
        self.energy += 25
        return self
    
    def eat(self):
        print(f"{self.name} is eating.")
        self.energy += 5
        self.health += 10
        print(self.energy)
        print("yumuuuy", self.health)
        return self
    
    def play(self):
        print(f"{self.name} is playing.")
        self.health += 5
        print(self.health)
        return self
    
    def noise(self):
        print(f"{self.name} is noisy!.")
        return self
        