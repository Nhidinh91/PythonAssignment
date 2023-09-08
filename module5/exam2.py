numbers = []
number = input("Please enter a number: ")
while True:
    if number == "":
        break
    number = float(number)
    numbers.append(number)
    number = input("Please enter a number, or enter to stop: ")

list_numbers = sorted(numbers, reverse=True)
print(list_numbers)
print(list_numbers[:5])
