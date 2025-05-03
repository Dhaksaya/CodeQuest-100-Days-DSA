N=int(input("Enter the number of terms: "))
sum=0
fib_list=[0]
if(N<=0):
    print("No elements !!")
else:
    for i in range (1,N):
        if(i==1 or i ==2):
            fib_list.append(1)
        else:
            sum=fib_list[-1]+list[-2]
            fib_list.append(sum)
    print("Fibonaci sequence: "," ".join(map(str,fib_list)))
#using loop instead of recurssive function to avoid more time complexity
#the order of time complexity for this loop is O(n) but for the recurssive function has O(2^n)