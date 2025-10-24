# Program to calculate factorial of a number

# Taking input from user
num = int(input("Enter a non-negative integer: "))

# Initialize factorial
factorial = 1

# Check for negative numbers
if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}")
