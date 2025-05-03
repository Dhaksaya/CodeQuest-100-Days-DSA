
N=input("Enter N:");
f=1;
for i in N:
    if int(i)%2==0:
        print(int(i),end=' ');
        f=0;
if f==1:
   print("No even digits found!");