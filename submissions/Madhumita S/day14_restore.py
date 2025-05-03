s = input("Input: ")
l = [ord(s[i]) for i in range(0,len(s))]
p=[]
for i in range(0,len(l)):
    if l[i]==ord('_'):
        if l[i+1]-l[i-1] == 2:
            p.append(l[i-1]+1)
    else:
        p.append(l[i])
print("Restored string: ",''.join([chr(p[i]) for i in range(0,len(p))]))