
k=input("Enter a sentence:").split(" ")
b=str(k).lower
c=['a','e','i','o','u']
d=0
e=0
for i in k:
    for j in i:
        if j in c:
            d=d+1
        else:
            e=e+1
print("Consonants:",e)
print("Vowels:",d)