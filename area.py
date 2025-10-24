import math

# Rectangle
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
area_rectangle = length * width
perimeter_rectangle = 2 * (length + width)

print("\n--- Rectangle ---")
print(f"Area: {area_rectangle}")
print(f"Perimeter: {perimeter_rectangle}")

# Circle
radius = float(input("\nEnter radius of circle: "))
area_circle = math.pi * radius ** 2
perimeter_circle = 2 * math.pi * radius

print("\n--- Circle ---")
print(f"Area: {area_circle:.2f}")
print(f"Circumference: {perimeter_circle:.2f}")

# Triangle
a = float(input("\nEnter side a of triangle: "))
b = float(input("Enter side b of triangle: "))
c = float(input("Enter side c of triangle: "))

# Using Heron's formula for area
s = (a + b + c) / 2
area_triangle = math.sqrt(s * (s - a) * (s - b) * (s - c))
perimeter_triangle = a + b + c

print("\n--- Triangle ---")
print(f"Area: {area_triangle:.2f}")
print(f"Perimeter: {perimeter_triangle}")
