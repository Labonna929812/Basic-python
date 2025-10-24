# Program to find the grade of a student based on marks

# Taking marks as input
marks = float(input("Enter your marks (out of 100): "))

# Checking grade conditions
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

# Displaying the result
print(f"Your Grade is: {grade}")
