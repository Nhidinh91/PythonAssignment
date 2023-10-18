number = int(input("Please enter an integer:"))
a = 1
for no in range(1, number):
    if number % no == 0:
        a += 1

if a <= 2:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
