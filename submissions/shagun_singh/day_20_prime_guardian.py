#prime calculator
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Taking input from the user
num = int(input("Enter a positive integer: "))

# Checking if the number is prime
if is_prime(num):
    print("Prime")
else:
    print("Not Prime")
