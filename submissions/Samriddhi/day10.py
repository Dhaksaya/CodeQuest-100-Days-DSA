k=input("Enter")
a=0 #to check if the length of the string is greater than or equal to 8
b=0 #to check if the string contains at least one uppercase letter
c=0 #to check if the string contains at least one lowercase letter
d=0 #to check if the string contains at least one digit
e=0 #to check if the string contains at least one special character
if len(k)>=8:
    a=1
for i in k:
    if i.isupper():
        b=1
    elif i.islower():
        c=1
    elif i.isdigit():
        d=1
    elif i in ['@','!','#','$','%','^','&','*']:
        e=1
if a==1 and b==1 and c==1 and d==1 and e==1: #if all conditions are true then the password is valid
    print("Valid Password")
else:
    print("Invalid Password")