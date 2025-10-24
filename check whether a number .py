# Program to check if a number is positive, negative, or neutral

# Taking input from the user
num = float(input("Enter a number: "))

# Checking the number
if num > 0:
    print(f"{num} is Positive")
elif num < 0:
    print(f"{num} is Negative")
else:
    print(f"{num} is Neutral (Zero)")
