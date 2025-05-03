import math
# Take input from the user
num = int(input("Enter a number: "))
# Check for prime
if num <= 1:
    print("Not a prime")
else:
    is_prime = True
    for i in range(2,int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break
    print("Prime" if is_prime else "Not Prime")        