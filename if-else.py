# Program to find the greatest number among three numbers

# Taking input from user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

# Comparing using if-else
if a >= b and a >= c:
    print(f"The greatest number is: {a}")
elif b >= a and b >= c:
    print(f"The greatest number is: {b}")
else:
    print(f"The greatest number is: {c}")
