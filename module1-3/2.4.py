number1 = int(input("Please enter 3 integer numbers. The first one ="))
number2 = int(input("The second one ="))
number3 = int(input("The third one ="))
sum = number1+number2+number3
product = number1*number2*number3
average = sum/3
print("The sum of the numbers is", str(sum))
print("The product of the numbers is", str(product))
print(f"The average of the numbers is {average:0.1f}")