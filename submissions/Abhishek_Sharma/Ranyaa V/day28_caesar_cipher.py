
s=input("Enter cipher text:")
n=int(input("Enter shift value:"))
r=[]
for i in s:
    if i.isalpha():
        s1=ord(i)-n
        if i.islower():
            if s1<ord('a'):
                s1+=26
        elif i.isupper():
            if s1<ord('A'):
                s1+=26
        r.append(chr(s1))
    else:
        r.append(i)
            
print("Decoded Message:","".join(r))

