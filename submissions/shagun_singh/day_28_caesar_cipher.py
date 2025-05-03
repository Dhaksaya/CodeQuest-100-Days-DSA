def decode_ciphered_text(cipher_text, shift):
    decoded_message = ""
    for char in cipher_text:
        if char.isalpha():  # Check if the character is a letter
            if char.islower():  # Handle lowercase letters
                decoded_message += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            elif char.isupper():  # Handle uppercase letters
                decoded_message += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            decoded_message += char  # Leave non-alphabetical characters unchanged
    return decoded_message

# Example usage
cipher_text = input("Enter cipher text: ")
shift = int(input("Enter shift value: "))
decoded_message = decode_ciphered_text(cipher_text, shift)
print("Decoded Message:", decoded_message)
