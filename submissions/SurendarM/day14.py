a=input()
b='abcedefghijklmnopqrstuvwxyz'
for i in a:
    if i in b:
        print(i,end='')
        c=ord(i)
    else:
        print(chr(c+1),end='')