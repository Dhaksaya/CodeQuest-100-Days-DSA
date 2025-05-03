# Day 11 - Sorting the Instructions

# Take user input as a string
input_number = input("Enter number: ")

# Convert the input string into a list of integers
number_list = list(map(int,input_number.split()))

# Sort the list
number_list.sort()

# Print the sorted list
print("Sorted List:", *number_list)