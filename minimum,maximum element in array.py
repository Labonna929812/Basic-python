# Program to find maximum and minimum elements in an array

# Taking the size of the array
n = int(input("Enter the number of elements in the array: "))

# Initialize an empty list
arr = []

# Reading elements from the user
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

# Finding maximum and minimum
maximum = max(arr)
minimum = min(arr)

# Displaying the result
print(f"The maximum element in the array is: {maximum}")
print(f"The minimum element in the array is: {minimum}")
