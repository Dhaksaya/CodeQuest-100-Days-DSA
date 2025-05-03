modules=input("Enter module scores (space-seperated): ")
flag=0
module_scores=list(map(int,modules.split()))
for i in module_scores :
    if(i<50):
        flag=flag+1
        if(flag==1):
            print("Modules to debug: ",end="")
        print(i,end=" ")
    else:
        continue
if(flag==0):
    print("All modules are working fine!")
