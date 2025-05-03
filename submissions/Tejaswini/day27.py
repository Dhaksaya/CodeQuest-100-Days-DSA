
a=input("Enter module scores:").split(" ")
s=[]
b=0
for i in a:
    if (int(i)<50):
        s.append(i)
        b=1
k=" ".join(s)
if(b==0):
    print("All modules are working fine!")
else:
    print("Modules to debug",k)