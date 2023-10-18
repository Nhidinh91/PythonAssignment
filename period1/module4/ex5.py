
number_input = 1
while True :
    username = input("Please enter your user name: ")
    password = input("Please enter your password: ")

    if number_input == 5:
        print("Access denied")
        break

    if username == "python" and password == "rule":
        print("Welcome!")
        break
    else :
        number_input+=1