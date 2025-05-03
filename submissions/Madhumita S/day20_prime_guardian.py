import math
n=int(input("Enter a number: "))
l = [i for i in range (1,int(math.sqrt(n)+1)) if n%i==0]
if len(l)==1:
    print("Prime")
else:
    print("Not Prime")