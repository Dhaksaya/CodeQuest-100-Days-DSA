#fibonacci series
N=int(input("Enter number of terms:"))
a=0#initializing a to 0
b=1#initializing b to 1
print("Fibonacci series:")
for i in range(N):#looping from 0 to N
    print(a,end=' ')#printing a
    c=a+b#calculating c
    a=b#updating a to b
    b=c#updating b to c

