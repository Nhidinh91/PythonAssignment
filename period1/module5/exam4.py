cities = []
for number in range(1, 6):
    enter = input("Please enter a city:\n")
    cities.append(enter)
print("Names of the cities in list:\n")
for index, item in enumerate(cities, start=1):
    print(f"{index}/{item}")
