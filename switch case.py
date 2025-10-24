# Simple Calculator using match-case (Python 3.10+)

# Taking inputs
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nSelect Operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("\nEnter your choice (+, -, *, /): ")

# Using match-case (acts like switch-case)
match choice:
    case '+':
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    case '-':
        print(f"Result: {num1} - {num2} = {num1 - num2}")
    case '*':
        print(f"Result: {num1} * {num2} = {num1 * num2}")
    case '/':
        if num2 != 0:
            print(f"Result: {num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operation! Please choose +, -, *, or /.")
