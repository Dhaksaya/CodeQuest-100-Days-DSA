# Take input from the user
n = int(input("Enter the number of terms for the Fibonacci sequence: "))

# Generate and print the Fibonacci sequence
a, b = 0, 1
print("The Fibonacci sequence:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
