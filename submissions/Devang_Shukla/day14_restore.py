# Day 14 - Restore the Missing Code

# Input the string
input_str = input("Enter string: ")

# Convert the string to a list for mutability
chars = list(input_str)

# Loop through the string 
for i in range(1, len(chars)-1):
    if chars[i] == '_':
        if chars[i -1] != '_' and chars[i+1] != '_':
            prev_char = chars[i -1]
            chars[i] = chr(ord(prev_char)+1)

# Join the list back to string and point the result
restored = ''.join(chars)
print("Restored string:", restored)