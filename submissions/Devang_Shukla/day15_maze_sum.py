# Day 15 : Maze Sum Puzzle

# Take input from the user
number = input("Enter number: ").split()

# Convert each item in the list to an integer
numbers = [int(num) for num in number]

# Calculate the sum 
total_sum = sum(numbers)

# Print the secret code
print("Secret Code:", total_sum)