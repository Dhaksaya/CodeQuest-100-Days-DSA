import string
s=input("Enter a sentence:")

for punct in string.punctuation:
    s=s.replace(punct,"")
s2=s.split()
maxlen=0
longword=""
for i in range(len(s2)):
    if len(s2[i])>maxlen:
        maxlen=len(s2[i])
        longword=s2[i]
print(f"Longest word:{longword}")