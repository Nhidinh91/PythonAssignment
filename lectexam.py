numbers = []

while True:
    number = float(input("Please enter a number ( a negative number will stop the program): "))
    if number < 0:
        numbers.append(number)
        break
    numbers.append(number)
for index,item in enumerate(numbers,start=1):
    print(f"{index}: {item}")

