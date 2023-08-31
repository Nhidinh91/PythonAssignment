length = float(input("Please enter the length of a zander in centimeters:\n"))
if length >= 42:
    print("It meets the size limit. You can keep it")
else:
    print("Please release the fish back into the lake. The caught fish was", str(42 - length),
          "centi below the size limit")
