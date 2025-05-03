# Input: Enter numbers separated by spaces
numbers = input("Enter numbers: ").split()

# Convert the list of strings to integers
numbers = [int(num) for num in numbers]

# Sort the list in ascending order
numbers.sort()

# Output: Print the sorted list as the key to unlock the hidden message
print("Sorted Data:", " ".join(map(str, numbers)))
