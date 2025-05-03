
a=input("Enter numbers:").split(" ")
l=len(a)
b=[]
for i in range(l):
    b.append(chr(int(a[i])))
s="".join(b)
print("Decoded message:",s)