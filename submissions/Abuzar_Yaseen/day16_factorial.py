def fact(n):
    if(n==0 or n==1):
        return 1
    return n *fact(n-1)
number = int(input("Enter a number: "))
factorial = fact(number)
print("Factorial of ",number,"is", factorial)