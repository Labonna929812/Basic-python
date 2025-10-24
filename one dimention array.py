# Program to read and print elements of a one-dimensional array

# Taking the size of the array
n = int(input("Enter the number of elements in the array: "))

# Initialize an empty list
arr = []

# Reading elements from the user
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

# Printing the array elements
print("\nThe elements of the array are:")
for i in range(n):
    print(arr[i], end=" ")
