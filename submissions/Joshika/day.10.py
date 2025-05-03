import string
s=0
a=input("Enter your password:")
if (len(a)>=8):
    s=1
if (a.isupper()):
    s=2
if (a.islower()):
    s=3
if (a.isdigit()):
    s=4
for i in a:
    if i in string.punctuation:
        s=s+1
if(s>4):
    print("strong password")
else:
    print("weak password")