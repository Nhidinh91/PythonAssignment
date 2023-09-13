import random
def roll_dice():
    roll = random.randint(1,6)
    return roll
time = 0
while True:
    roll = roll_dice()
    time += 1
    if roll == 6:
        print(f"Roll {time}: {roll}")
        break
    print(f"Roll {time}: {roll}")