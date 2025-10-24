# Program to reverse a given number

# Taking input from user
num = int(input("Enter a number: "))

# Store the original number
original_num = num
reversed_num = 0

# Reversing the number
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

# Display the result
print(f"The reverse of {original_num} is {reversed_num}")
