
a=input("Enter binary number:").split(" ")
l=len(a)
p=0
for i in range(0,l):
    p=p+((int(a[l-i-1]))*(2**i))
print("Decimal:",p)