list1=[]
n=0
print("Enter numbers:",end=" ")
while(n>=0):
    n=int(input())
    if(n>=0):
        list1.append(n) 
print("Sorted Data:"," ".join((map(str,sorted(list1)))))
