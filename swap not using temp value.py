# Program to swap two numbers without using a temporary variable

# Taking input from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\nBefore swapping:")
print("a =", a)
print("b =", b)

# Swapping without using a temporary variable
a, b = b, a

print("\nAfter swapping:")
print("a =", a)
print("b =", b)
