# Initialize the first two terms in a way that the first Fibonacci number becomes 0
t1 = -1
t2 = 1
nxt = 0

# Take number of terms from the user
n = int(input("Enter the number of terms : "))

# Print the label for the Fibonacci sequence
print("Fibonacci sequence : ", end='')

# Generate and print Fibonacci sequence up to n terms
for i in range(1, n + 1):
    # Calculate the next term in the sequence
    nxt = t1 + t2

    # Print the current term
    print(nxt, end=' ')

    # Update previous two terms for the next iteration
    t1 = t2
    t2 = nxt
