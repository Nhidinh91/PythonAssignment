grades = [90, 89, 80, 70, 60, 50]
for grade in grades:
    if grade >=90:
        print(f"Your score is {grade} grade A")
    elif 80<= grade <=89:
        print(f"Your score is {grade} grade B")
    elif 70<= grade <=79:
        print(f"Your score is {grade} grade C")
    elif 60<= grade <=69:
        print(f"Your score is {grade} grade D")
    else:
        print("See you again!")
