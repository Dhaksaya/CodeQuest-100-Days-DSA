s = str(input("Enter string : "))
result = ""

for i in range(len(s)):
    if s[i] == "_":
        next_char = chr(ord(result[-1]) + 1)
        result += next_char
    else:
        result += s[i]

print("Restored string : ", result)
