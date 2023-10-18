import random

num_dice = int(input("How many dice do you want to roll: "))
sum_roll = 0
for num_dice in range(num_dice):
    roll = random.randint(1, 6)
    print(roll)
    sum_roll += roll
print(f"The sum of the numbers:\n{sum_roll}")
