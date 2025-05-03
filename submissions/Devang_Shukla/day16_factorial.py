def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
#Input from thr user
num = int(input("Enter a number: "))

# Validate non-negative input
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(num)
    print(f"Factorial of {num} is {result}")    