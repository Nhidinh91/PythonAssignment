cabinclass = input("Enter your cabin class: ")
if cabinclass == "LUX":
    print("It's upper-deck cabin with a balcony")
elif cabinclass == "A":
    print("It's above the car deck, equipped with a window")
elif cabinclass == "B":
    print("It's windowless cabin above the car deck")
elif cabinclass == "C":
    print("It's windowless cabin below the car deck")
else:
    print("Invalid cabin class")