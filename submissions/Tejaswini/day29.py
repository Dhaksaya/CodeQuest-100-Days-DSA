
a=input("Enter list 1:").split(" ")
b=input("Enter list 2:").split(" ")
c=[]
l=0
for i in a:
    if i in b:
        c.append(i)
        l=1
d=" ".join(c)
if(l==1):
    print("Common elements:",d)
else:
     print("No commom elements found!")