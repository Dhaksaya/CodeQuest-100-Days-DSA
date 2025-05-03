n=input("Enter N: ")
a=0
l=[]
for i in range(0,len(n)):
    if int(n[i])%2==0:
        l.append(n[i])
        a+=1
if a==0:
    print("No even digits found!")
else:
    print("Even digits: ",end='')
    for i in range(0,len(l)):
        print(l[i],end=' ')