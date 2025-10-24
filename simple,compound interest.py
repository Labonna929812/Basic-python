# Program to calculate Simple Interest and Compound Interest

# Taking user input
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time (in years): "))

# Calculating Simple Interest
simple_interest = (principal * rate * time) / 100

# Calculating Compound Interest
compound_interest = principal * ((1 + rate / 100) ** time) - principal

# Display results
print("\n--- Interest Calculation ---")
print(f"Principal Amount: {principal}")
print(f"Rate of Interest: {rate}%")
print(f"Time: {time} years")
print(f"Simple Interest: {simple_interest:.2f}")
print(f"Compound Interest: {compound_interest:.2f}")
