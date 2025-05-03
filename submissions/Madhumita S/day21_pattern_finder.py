l=list(map(int,input("Enter numbers: ").split()))
sum=0
for i in range(1,len(l),2):
    sum+=l[i]
print("Hidden Key: ",sum)