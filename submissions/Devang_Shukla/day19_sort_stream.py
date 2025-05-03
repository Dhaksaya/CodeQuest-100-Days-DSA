# Take input from user
numbers = input("Enter number: ").split()

# Convert each element to integer
int_list = [int(num) for num in numbers]

# Sort the list in ascending order
int_list.sort()

# Print the sorted list
print("Sorted Data:", *int_list)