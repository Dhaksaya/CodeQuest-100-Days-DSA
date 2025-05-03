
s=input("Enter a sentence:")
s=s.lower()
v=0
c=0
for i in s:
    if i.isalpha():
        if i in 'aeiou':
            v+=1
        else:
            c+=1
print(f"Vowels:{v}")
print(f"Consonants:{c}")

