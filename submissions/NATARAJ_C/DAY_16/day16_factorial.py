def factorial(number):
    if number == 0:
        return 1
    else:
        return number*(factorial(number-1))

n=int(input("Enter the number for factorial value: "))
print(factorial(n))