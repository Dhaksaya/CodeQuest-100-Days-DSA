p=input("Enter your password: ")
if len(p)<8:
    print("Weak Password ( Password should have atleast 8 characters )")
else:
    u=l=d=s=0
    for i in range(0,len(p)):
        if p[i].isupper() : 
            u+=1
        elif p[i].islower():
            l+=1
        elif p[i].isdigit():
            d+=1
        elif p[i]!=" ":
            s+=1
    c=[u,l,d,s]
    if all(c):
        print("Strong Password")
    else:
        print("Weak Password ( Missing ",end="")
        a=c.count(0)
        m={0:"uppercase letter ",1:"lowercase letter ",2:"Digit ",3:"special character "}
        for i in range(0,len(c)):
            if c[i]==0:
                print(m[i],end='')
                a-=1
                if a!=0:
                    print("and ",end='')
        print(")")