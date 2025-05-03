k=int(input("Enter a number:"))#taking input from user
s=1#initializing s to 1
for i in range(1,k+1):#looping from 1 to k+1
    s=s*i#calculating factorial
print("Factorial of",k,"is",s)#printing the factorial of k