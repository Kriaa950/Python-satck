# Create a Ninja class with the ninja attributes listed above 
class Ninja:
# challenge 1 initialize ninja attributes
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
# challenge 2 implement the the methods
    def walk(self):
        print(f"{self.first_name} is  walking with {self.pet.name}.")
        self.pet.play()
        return self
    def feed(self):
        print(f"{self.first_name} is feeding {self.pet.name}.")
        self.pet.eat()
        return self
    def bathe(self):
        print(f"{self.first_name} is bathing {self.pet.name}.")
        self.pet.noise()
        return self
