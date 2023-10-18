import random
def roll_dice(maximum):
    roll = random.randint(1,maximum)
    return roll
time = 0
maximum_number = int(input("Please enter the maximum number on the dice:\n"))
while True:
    roll = roll_dice(maximum_number)
    time += 1
    if roll == maximum_number:
        print(f"Roll {time}: {roll}")
        break
    print(f"Roll {time}: {roll}")