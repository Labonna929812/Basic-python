# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False  # 0 and 1 are not prime
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Input from user
num = int(input("Enter a number to check if it is prime: "))

# Check and display result
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
