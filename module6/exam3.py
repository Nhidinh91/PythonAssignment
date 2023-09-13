def convert(gallon) :
    litres = gallon*3.785411784
    return litres
while True:
    volumn_gallon = float(input("Please input a volumn in gallons: "))
    if volumn_gallon <0:
        print("The execution stopped.")
        break
    print(f"{volumn_gallon} gallons = {convert(volumn_gallon):.2f} litres")