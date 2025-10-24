# Program to find the maximum of three numbers using logical operators

# Taking input from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Using logical operators to find the maximum
if (a >= b) and (a >= c):
    maximum = a
elif (b >= a) and (b >= c):
    maximum = b
else:
    maximum = c

# Display the result
print("The maximum number is:", maximum)
