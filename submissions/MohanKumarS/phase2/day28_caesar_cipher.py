def caesar_cipher(word, shift):
    decoded = ''
    for ch in word:
        if ch.isalpha():  # Only shift letters
            value = ord(ch) - shift
            if ch.islower():
                while value < ord('a'): # suppose if the ord('b') = 98 -> value=98-5=>93 -> we need to add 26 to reverse only through small alphabhat.
                    value += 26
            elif ch.isupper():
                while value < ord('A'): # suppose if the ord('B') = 66 -> value=66-5=>61 -> we need to add 26 to reverse only through Capital alphabhat.
                    value += 26
            decoded += chr(value)
        else:
            decoded += ch 
    return decoded

word = input("Enter cipher text: ")
shift = int(input("Enter shift value: "))
print("Decoded Message:", caesar_cipher(word, shift))
