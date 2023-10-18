import math

talent = float(input("Enter talents:\n"))
pound = float(input("Enter pounds:\n"))
lot = float(input("Enter lots:\n"))
total = talent * 20 * 32 * 13.3 + pound * 32 * 13.3 + lot * 13.3
kg = total // 1000
gram = total - kg * 1000
print(f"The weight in modern units:\n{kg:0.0f} kilograms and {gram:0.2f} grams.")
