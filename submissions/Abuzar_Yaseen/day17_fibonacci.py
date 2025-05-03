def fibonacci(n):
    num1 = 0
    num2 = 1
    if n <= 0:
        return
    elif n ==1:
        print(num1,end=" ")
    else:
        print(num1,end=" ")
        print(num2,end=" ")
        for _ in range(2,n):
            num = num1 + num2
            print(num,end=" ")
            num1 = num2
            num2 = num
number = int(input("Enter the number of terms: "))
print("Fibonacci sequence: ",end=" ")
fibonacci(number)
