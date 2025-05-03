# Function to ask for the secret word and print it multiple times
def secret_word():
    secret = input("Enter the secret word: ")  # Prompt the user to enter the secret word
    
    # Repeat the word 5 times
    for _ in range(5):
        print(secret)

# Call the function
secret_word()
