# Program to find the minimum of two numbers using the conditional (ternary) operator

# Taking input from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Using ternary operator
minimum = a if a < b else b

# Display the result
print("The minimum number is:", minimum)
