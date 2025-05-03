n=str(input("Enter N:"))
l=0
for i in n:
    if (int(i)%2==0):
        print(i,end=" ")
        l=l+1
if(l==0):
    print("No even digits found")
    

              