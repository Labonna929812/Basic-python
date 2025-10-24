# Program to perform Linear Search and Binary Search

# Function for Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return index if found
    return -1  # Return -1 if not found

# Function for Binary Search (array must be sorted)
def binary_search(arr, target):
    arr.sort()  # Ensure the array is sorted
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Main program
n = int(input("Enter the number of elements in the array: "))
arr = []
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

target = int(input("Enter the number to search for: "))

# Linear Search
linear_result = linear_search(arr, target)
if linear_result != -1:
    print(f"Linear Search: Element found at index {linear_result}")
else:
    print("Linear Search: Element not found")

# Binary Search
binary_result = binary_search(arr, target)
if binary_result != -1:
    print(f"Binary Search (sorted array): Element found at index {binary_result}")
else:
    print("Binary Search: Element not found")
