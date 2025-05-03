
n=list(map(int,input("Enter numbers:").split()))
s=""
for i in n:
    s+=chr(i)
print(f"Decoded Message:{s}")