import random

number_points = int(input("Enter the number of points: "))
number = 1
a = 0
while number <= number_points:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x ** 2 + y ** 2 <= 1:
        a += 1
    number = number + 1
pi = 4 * a / number_points
print(f"Pi = {pi}")
