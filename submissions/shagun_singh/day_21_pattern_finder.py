# Take space-separated numbers as input
numbers = list(map(int, input("Enter numbers: ").split()))

# Initialize the sum
hidden_key = 0

# Iterate through the numbers list using 1-based indexing for even positions
for index, number in enumerate(numbers, start=1):  # 1-based indexing
    if index % 2 == 0:  # Check if position is even
        hidden_key += number

# Print the result
print(f"Hidden Key: {hidden_key}")
