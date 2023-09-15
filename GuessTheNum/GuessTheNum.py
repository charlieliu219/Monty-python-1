import random

randomNum = random.randint(0, 100)

while (True):
    userNum = int(input("Guess a number: "))
    if userNum < randomNum:
        print("Too low!")
    elif userNum > randomNum:
        print("Too high!")
    else:
        print("You got it!")
        break
    