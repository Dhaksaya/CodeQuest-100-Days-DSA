
n=list(map(int,input("Enter module scores (space-separated):").split()))
s=[]
for i in range(len(n)):
    if n[i]<=50:
        s.append(str(n[i]))
    
if len(s)==0:
    print("All modules are working fine!")
else:
    print("Modules to debug:"," ".join(s))