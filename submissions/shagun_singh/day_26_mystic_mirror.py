# Function to count vowels and consonants
def count_vowels_and_consonants(sentence):
    # Convert the input to lowercase
    sentence = sentence.lower()
    vowels = "aeiou"
    vowels_count = 0
    consonants_count = 0

    # Loop through each character in the sentence
    for char in sentence:
        if char.isalpha():  # Check if it's an alphabet
            if char in vowels:
                vowels_count += 1
            else:
                consonants_count += 1

    # Print the counts
    print("Vowels:", vowels_count)
    print("Consonants:", consonants_count)

# Example usage
sentence = input("Enter a sentence: ")
count_vowels_and_consonants(sentence)
