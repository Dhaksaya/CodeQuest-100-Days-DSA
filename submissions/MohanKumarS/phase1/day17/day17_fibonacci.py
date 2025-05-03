n = int(input("Enter the number of terms: "))
def fibonacci(n): # user defined function for fibonacci
    if n <= 1:
        return n # if n == 0 -> it returns 0, similary if n == 1 -> it returns 1
    else:
        return fibonacci(n-1) + fibonacci(n-2) # recursive function -> to sum up previous two results
print("Fibonacci Sequence: ", end='')
for i in range(n): # print the fibonacci sequence
    print(fibonacci(i), end=' ')

# 0 1 1 2 3 5 8 13 21