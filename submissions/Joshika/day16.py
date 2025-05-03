a=int(input("Enter a number:"))
def fact(n):
    if n==(0|1):
        return 1
    else:
        return n*fact(n-1)
s=fact(a)
print("Factorial of a is",s)