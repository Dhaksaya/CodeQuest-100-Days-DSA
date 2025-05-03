#Factorial Calculator
num = int(input("Enter a number: "))

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("Factorial of", num, "is", factorial(num)) 
