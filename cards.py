import random

cards = ["jack" , "queen" , "king"]

def main():
    random.seed(0)
    print(random.choices(cards , weights=[100 , 75 , 25] , k=2))

main()