a = input("Enter text: ").split(" ")
l = len(a)
c = 0

while l > 0:
    i = a[0] 
    c = 0
    for j in range(l):  
        if i == a[j]:
            c += 1
    print(i, ":", c)
    a = [x for x in a if x != i]
    l = len(a) 

