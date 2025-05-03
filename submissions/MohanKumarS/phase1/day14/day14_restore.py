s = input("Enter string: ")

result = ''
i = 0
while i < len(s):
    if s[i] != '_':
        result += s[i]
        i += 1
    else:
        # If underscore is at start or end, skip it
        if i == 0 or i + 1 >= len(s):
            i += 1
            continue
        prev_char = result[-1]
        next_char = s[i + 1]

        # Fill the missing characters depending on direction
        if ord(prev_char) < ord(next_char):
            # Forward filling
            for ascii_val in range(ord(prev_char) + 1, ord(next_char)):
                result += chr(ascii_val)
        elif ord(prev_char) > ord(next_char):
            # Reverse filling
            for ascii_val in range(ord(prev_char) - 1, ord(next_char), -1):
                result += chr(ascii_val)
        # else: chars are equal, nothing to fill
        i += 1  # skip the underscore
print("Restored string: ", result)

