import random
threedigits = [random.randint(0, 9) for _ in range(3)]
fourdigits = [random.randint(1, 6) for _ in range(4)]
print("Random 3-digit combination, each number is between 0 and 9:\n", threedigits )
print("Random 4-digit combination, each number is between 1 and 6:\n", fourdigits)