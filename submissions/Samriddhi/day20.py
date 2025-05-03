#prime number
k=int(input("Enter a number: "))#taking input from the user
c=0#initializing the counter to 0
for i in range(1,k+1):#looping from 1 to k
    if k%i==0:#checking if k is divisible by i
        c+=1#incrementing the counter if it is divisible
if c==2:#checking if the counter is 2
            print("Prime number")#if it is, print that it is a prime number
else:
            print("Not a prime number")