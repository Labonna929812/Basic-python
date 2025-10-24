# Program to count positive, negative, zero, even, and odd elements in an array

# Taking the size of the array
n = int(input("Enter the number of elements in the array: "))

# Initialize an empty list
arr = []

# Reading elements from the user
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

# Initialize counters
positive = negative = zero = even = odd = 0

# Counting
for num in arr:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1
    
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

# Displaying the results
print(f"Positive numbers: {positive}")
print(f"Negative numbers: {negative}")
print(f"Zeros: {zero}")
print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")
