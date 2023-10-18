def sum(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum
list_number = [1,2,6,8,10]
print(f"Sum of all number in the list = {sum(list_number)}")