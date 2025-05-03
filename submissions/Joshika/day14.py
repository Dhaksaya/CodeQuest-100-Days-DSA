a = str(input())
b = a.lower()
s = ""
l = 0  
for i in b:
    if ord(i) != 95:  
        s = s + i      
        p = ord(i)      
    else:
        s = s + (chr(p+1)) 
print("Restored string", s)