n=input("Enter numbers: ")
l=[]
sum=0
for i in n:
    if(i==" "):
        continue
    else:
        l.append(int(i))
print(l)
for i in range(1,len(l),2):
    sum=sum+l[i]
print(sum)
    
