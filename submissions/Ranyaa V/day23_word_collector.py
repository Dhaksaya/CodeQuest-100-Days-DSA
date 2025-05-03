
import string
def freq(s):
    text=s.lower()
    
    for punct in string.punctuation:
        text=text.replace(punct,"")
    word=text.split()
    d={}
    for j in word:
        d[j]=d.get(j,0)+1
    for k,v in d.items():
        print(f"{k}:{v}")
s=input("Enter text:")
freq(s)