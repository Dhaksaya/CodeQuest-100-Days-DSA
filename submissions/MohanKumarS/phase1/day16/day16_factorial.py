n = int(input("Enter a number: ")) # get the number from the user to find the factorial
def fact(n): # user-defined function for finding a factorial of a number
    if n == 0:     # if n == 0, 0! = 1 (hence, return 1)
        return 1
    else:           
        return n * fact(n-1) 
#Take n = 5;
#n * fact(n-1)
#=>5*fact(4) =>5*4*fact(3) =>5*4*3*fact(2) =>5*4*3*2*fact(1) =>5*4*3*2*1*fact(0) =>5*4*3*2*1*1 => 120

print("Factorial of {} is {}".format(n, fact(n)))