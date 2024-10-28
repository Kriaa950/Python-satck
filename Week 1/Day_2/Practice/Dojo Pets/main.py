from ninja import Ninja
from pet import Pet

my_pet = Pet("rex", "Dog", ["Fetch, roll over"])
ninja = Ninja("Abdallah", "Ariaa", "dog Treats", "Dog food", my_pet)

ninja.walk()
ninja.feed()
ninja.bathe()

