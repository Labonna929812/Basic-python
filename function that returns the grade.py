# Function to determine grade
def get_grade(marks):
    if marks < 0 or marks > 100:
        return "Invalid marks"
    elif marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B+"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

# Input from user
marks = float(input("Enter the marks of the student: "))
grade = get_grade(marks)
print(f"The grade of the student is: {grade}")
