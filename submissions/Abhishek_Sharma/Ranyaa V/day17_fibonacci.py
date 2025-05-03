N=int(input("Enter the number of terms:"))
a=0
b=1
print(a,b,end=" ")
for i in range(N-2):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
    

    

