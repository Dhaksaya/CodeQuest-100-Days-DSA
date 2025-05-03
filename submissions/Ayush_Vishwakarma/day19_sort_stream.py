# Get input from the user and convert it to a list of integers
lst = list(map(int, input("Enter numbers: ").split()))

# Sort the list
lst.sort()

# Print the sorted list in the desired format
print("Sorted List:", *lst)
