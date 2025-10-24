# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Main program
num = int(input("Enter a number: "))

# Calling the function
result = check_even_odd(num)

# Displaying the result
print(f"The number {num} is {result}.")
