cipher_text = input("Enter cipher text: ")
shift = int(input("Enter shift value: "))
decoded_text = ""
for char in cipher_text:
    if char.isalpha():
        shifted = ord(char) - shift
        if char.islower():
            if shifted < ord('a'):
                shifted += 26
        elif char.isupper():
            if shifted < ord('A'):
                shifted += 26
        decoded_text += chr(shifted)
    else:
        decoded_text += char
print("\nDecoded Message:", decoded_text)

