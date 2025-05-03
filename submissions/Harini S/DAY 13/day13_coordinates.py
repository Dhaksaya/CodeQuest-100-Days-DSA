num=int(input("Enter N: "))
first=True
a=0
for i in str(num):
    if int(i)%2==0: 
        if first: 
            print("Even digits: ") 
            first=False
        print(i,end=' ')
        a+=1
if a==0:print("No even digits found!")