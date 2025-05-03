def generate_fibonacci(n):
    if n<= 0:
        print("Please enter a positive integer.")
    elif n == 1:
        print("Fibonacci sequence:0")
    else:
        a,b = 0,1
        print("Fibonacci sequence:", end=" ")
        print(a, end=" ")
        for _ in range(1 , n):
            print(b, end=" ")
            a, b = b, a + b
        print()
# Input from the user
terms = int(input("Enter the number of terms: "))
generate_fibonacci(terms)                     
        