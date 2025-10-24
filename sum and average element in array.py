# Program to calculate sum and average of elements in an array

# Taking the size of the array
n = int(input("Enter the number of elements in the array: "))

# Initialize an empty list
arr = []

# Reading elements from the user
for i in range(n):
    element = float(input(f"Enter element {i+1}: "))
    arr.append(element)

# Calculating sum
total = sum(arr)

# Calculating average
average = total / n

# Displaying results
print(f"Sum of the array elements: {total}")
print(f"Average of the array elements: {average}")
