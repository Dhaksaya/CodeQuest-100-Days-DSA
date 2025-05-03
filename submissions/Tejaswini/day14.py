
n=input("enter:");
l=[];
x=[];
for i in n:
    l.append(i);
for i in range(0,len(l)):
    if l[i].isalpha():
        x.append(l[i]);
    elif l[i]=="_":
        j=ord(l[i-1]);
        x.append(chr(j+1));

print(''.join(x));
        