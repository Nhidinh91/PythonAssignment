airport_data = {}
print("Input 1 to enter a new airport")
print("Input 2 to fetch the information of an existing airport")
print("Input 3 to quit")
while True:
    command = input("Choose what you want to do:")
    if command == "3":
        print("the program ends")
        break
    elif command == "1":
        code = input("Input the ICAO code: ")
        name = input("Input the name of the airport: ")
        airport_data[code] = name
    elif command == "2":
        code = input(" Please enter the ICAO code of the airport: ")
        if code in airport_data:
            print(f"The airport name of the ICAO code {code} is: {airport_data[code]} ")
        else:
            print("Unidentified code")
    else:
        print("Invalid input. Please choose 1 or 2 or 3")

