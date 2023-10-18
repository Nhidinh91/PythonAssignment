gender = input("What is your biological gender (female or male):\n")
hemoglobin = float(input("How much is your hemoglobin value in (g/l):\n"))
if gender == "female":
    if 117 <= hemoglobin <= 155:
        print("Your hemoglobin value is normal.")
    elif hemoglobin < 117:
        print("Your hemoglobin value is low.")
    else:
        print("Your hemoglobin value is high.")
elif 134 <= hemoglobin <= 167:
    print("Your hemoglobin value is normal.")
elif hemoglobin < 167:
    print("Your hemoglobin value is low.")
else:
    print("Your hemoglobin value is high.")
