import string

def word_frequency(text):
    # Convert text to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Split text into words
    words = text.split()
    
    # Create a dictionary to store word frequencies
    freq_dict = {}
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    
    # Print each word with its frequency
    for word, freq in freq_dict.items():
        print(f"{word}: {freq}")

# Example usage
user_input = input("Enter text: ")
word_frequency(user_input)
