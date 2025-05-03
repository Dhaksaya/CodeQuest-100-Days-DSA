n = int(input("Enter the number of terms: "))
a = 0
b = 1
print("Fibonacci sequence:",a,b,end=' ')
for i in range(0,n-2):
    c = a+b
    print(c,end=' ')
    a = b
    b = c