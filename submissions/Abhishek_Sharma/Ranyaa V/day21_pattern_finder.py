
num=list(map(int,input("Enter numbers:").split()))
h=0
for i in range(1,len(num),2):
    h=h+num[i]
print(f"Hidden Key:{h}")