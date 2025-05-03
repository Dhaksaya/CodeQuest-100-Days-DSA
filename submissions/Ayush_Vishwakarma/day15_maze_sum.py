# Take input from the user, split the input by spaces, convert each to an integer, and store in a list
l = list(map(int, input("Enter numbers : ").split()))

# Initialize a variable to store the sum of numbers
sum = 0

# Loop through each number in the list and add it to the sum
for i in l:
    sum += i

# Print the final sum as a "Secret code"
print("Secret code :", sum)
