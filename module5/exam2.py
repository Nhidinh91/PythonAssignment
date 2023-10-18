numbers = []

while True:
    number = input("Please enter a number or enter: ")
    if number == "":
        break
    number = float(number)
    numbers.append(number)


list_numbers = sorted(numbers, reverse=True)
print(list_numbers)
print(list_numbers[:5])
