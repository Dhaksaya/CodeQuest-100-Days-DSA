
a=int(input("Enter a positive number:"))
p=0
for i in range (2,11):
    if(a!=i):
        if(a%i==0):
            p=1
            continue
if (p==0):
    print("Prime")
else:
    print("Not prime")