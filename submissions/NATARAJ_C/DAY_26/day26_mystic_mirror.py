sentence=input("Enter a sentence: ")
vowels=['a','e','i','o','u','A','E','I','O','U']
Vowels=0
Consonants=0
for i in sentence:
    if(i in vowels):
        Vowels=Vowels+1
    elif(i==" "):
        continue
    else:
        Consonants=Consonants+1
print("Vowels:",Vowels)
print("Consonants:",Consonants)

