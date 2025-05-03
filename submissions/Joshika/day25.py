
a=input("Enter asentence:").split(" ")
p=0
for i in a:
    l=len(i)
    if(l>p):
        p=l
        s=i
        t=s
        l=0
    elif(l==p):
        s=t
print("Longest word:",s)

