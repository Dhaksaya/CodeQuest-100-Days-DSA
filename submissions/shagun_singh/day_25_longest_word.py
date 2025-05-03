def find_longest_word(sentence):
    words = sentence.split()  # Split the sentence into a list of words
    longest_word = max(words, key=len)  # Find the word with the maximum length
    return longest_word

# Get user input
sentence = input("Enter a sentence: ")
print("Longest word:", find_longest_word(sentence))
