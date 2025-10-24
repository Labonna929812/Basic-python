# Program to check whether a number is even or odd
# using both modulo and bitwise operators

# Taking input from the user
num = int(input("Enter a number: "))

# Using modulo operator
if num % 2 == 0:
    print(f"Using modulo: {num} is Even")
else:
    print(f"Using modulo: {num} is Odd")

# Using bitwise operator
if num & 1 == 0:
    print(f"Using bitwise: {num} is Even")
else:
    print(f"Using bitwise: {num} is Odd")
