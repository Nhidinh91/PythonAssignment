while True:
    number = int(input("Please enter an integer number: "))
    if number <= 0:
        print("Stop")
        break
    factorial = number
    for no in range(1, number):
        factorial *= no
    print(f"The factorial of the number {number} is {factorial}")
