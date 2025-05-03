list=[]
n=0
print("Enter numbers: ")
while True:
    n=int(input())
    if(n<0):
        break
    list.append(n)
print("Secret code:",sum(list))
