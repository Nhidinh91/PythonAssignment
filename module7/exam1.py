seasons = ("Winter", "Spring", "Summer", "Autumn")
month_number = int(input("Please enter a month number: "))
if 1<= month_number<= 12:
    season_index = (month_number%12)//3
    season = seasons[season_index]
    print(f"The season for month {month_number} is {season} ")