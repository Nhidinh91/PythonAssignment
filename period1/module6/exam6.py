def price_per_unit(diameter,price):
    price_per_squaremeter = price/(3.14*((diameter/2)**2)*10**(-4))
    return price_per_squaremeter
while True:
    diameter_first = float(input("Please input the diameter of two round pizzas in centimeters and their prices or enter stop to stop the program\n The diameter of the first pizza: "))
    if diameter_first == 0:
        break
    price_first= float(input("The price of the first pizza: "))
    diameter_second = float(input("The diameter of the second pizza: "))
    price_second = float(input("The price of the second pizza: "))
    if price_per_unit(diameter_first,price_first) > price_per_unit(diameter_second,price_second):
        print("The pizza 2 provides better value for money than 1")
    elif price_per_unit(diameter_first,price_first) < price_per_unit(diameter_second,price_second):
        print("The pizza 1 provides better value for money than 2")
    else:
        print("2 pizzas have the same value for money")