import random

houses = ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]

def sort(name):
    print(name, "is in", random.choice(houses))

sort("Harry")