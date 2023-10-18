import random

number = random.randint(1, 10)
guessnumber = int(input("Please guess a number from 1 to 10:"))
while guessnumber != number:
    if guessnumber > number:
        print("Too high")
    else:
        print("Too low")
    guessnumber = int(input("Please guess again:"))
print("Correct!")

