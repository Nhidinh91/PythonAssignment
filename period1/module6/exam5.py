def remove_uneven(list):
    even_number = []
    for number in list:
        if number % 2 == 0:
            even_number.append(number)
    return even_number


list_number = [1, 3, 5, 7, 8, 11, 9, 20, 6]
print(list_number)
print(remove_uneven(list_number))
