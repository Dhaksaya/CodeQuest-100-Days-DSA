# Get user input
numbers = input("Enter numbers: ")

# Convert numbers to ASCII characters
decoded_message = ''.join(chr(int(num)) for num in numbers.split())

# Print the result
print("Decoded Message:", decoded_message)
