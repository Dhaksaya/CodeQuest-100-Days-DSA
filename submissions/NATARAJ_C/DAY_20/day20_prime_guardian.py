N=int(input("Enter a number: "))
if(N<=2 or N%2==0):
    print("Not Prime")
else:
    for i in range(3,int(N**0.5)+1,2):
        if N%i==0:
            print("Not Prime")
            break
        else:
            print("Prime")