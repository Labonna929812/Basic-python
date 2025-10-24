# Program to determine whether a character is a vowel, consonant, digit, or special symbol

# Taking input
ch = input("Enter a single character: ")

# Checking the type of character
if ch.isalpha():  # Checks if it's a letter
    if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
        print(f"'{ch}' is a Vowel.")
    else:
        print(f"'{ch}' is a Consonant.")
elif ch.isdigit():  # Checks if it's a number
    print(f"'{ch}' is a Digit.")
else:
    print(f"'{ch}' is a Special Symbol.")
