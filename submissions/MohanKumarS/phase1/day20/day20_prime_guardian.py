import math # library file: inorder to use math function in code
def prime(n): # user-defined function for prime number checking
    if(n == 1): # 1 is neither prime nor composite number
        print("Neither Prime nor Composite")
        return 0
    else:
        for i in range(2, int(math.sqrt(n)) + 1):  # we need to check whether there is a factor for a number or not
          if(n % i == 0):
             print("Not Prime")
             return 0
        print("Prime")
        return 0

n = int(input("Enter a number: "))
prime(n)