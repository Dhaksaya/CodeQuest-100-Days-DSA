# Function to compute factorial using recursion
def fact(n):
    # If n is 0 or 1, return 1 since factorial of 0 and 1 is always 1
    if n == 1 or n == 0:
        return 1
    else:
        # Recursive case: Multiply n by the factorial of (n-1)
        return n * fact(n-1)

# Taking user input for the number whose factorial is to be calculated
num = int(input("Enter the number: "))

# Displaying the computed factorial
print("Factorial of", num, "is", fact(num))
