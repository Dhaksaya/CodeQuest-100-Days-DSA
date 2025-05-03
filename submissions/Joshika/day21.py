
a=input("Enter Numbers:").split(" ")
l=len(a)
s=0
for i in range (0,l):
    if(i%2!=0):
        s=s+int(a[i])
        
print("Hidden Key:",s)