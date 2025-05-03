# Step 1: Prompt the user to enter a message
# The input() function:
#   1. Displays the string argument as a prompt ("Enter the secret message: ")
#   2. Pauses program execution and waits for user input
#   3. Returns the user's input as a string
msg = input("Enter the secret message: ")

# Step 2: Reverse the string using Python's slice notation
# String slicing syntax: [start:stop:step]
# When all parameters are omitted with '::', it means:
# - start: beginning of string (implicit 0)
# - stop: end of string (implicit len(string))
# - step: -1 (process the string backwards)
# 
# Technical breakdown:
# - msg[::] would normally copy the entire string
# - Adding -1 as step makes it:
#   * Start at the last character (due to negative step)
#   * Move backwards through the string
#   * Stop at the first character
reversed_msg = msg[::-1]

# Step 3: Output the reversed string
# print() function:
#   1. Converts its arguments to strings if needed
#   2. Writes to standard output (usually the console)
#   3. Adds a newline by default
print(reversed_msg)