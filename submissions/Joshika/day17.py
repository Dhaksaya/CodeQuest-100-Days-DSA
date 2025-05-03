a=int(input("Enter a number:"))
b=0
c=1
for i in range(1,a+1):
    if(i==1):
        print(b,end=" ")
    if(i==2):
        print(c,end=" ")
    if(i>2):
        p=b+c
        b=c
        c=p
        print(p,end=" ")

    
    