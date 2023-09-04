enter = input("Please enter a number: ")
largest = float(enter)
smallest = float(enter)
while enter != "":
    enter = float(enter)
    if enter > largest:
        largest = enter

    if enter < smallest:
        smallest = enter

    enter = input("Please enter a number(or press Enter to quit): ")
print("The largest number", str(largest))
print("The smallest number", str(smallest))