# Program to check if a year is a leap year

# Taking input from the user
year = int(input("Enter a year: "))

# Leap year conditions:
# 1. Divisible by 4
# 2. Not divisible by 100, unless also divisible by 400
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is Not a Leap Year")
