def longest_word(word):
    longest_words = []
    long_len = len(word[0])
    longest_words.append(word[0])
    
    for i in range(1, len(word)):
        if len(word[i]) > long_len:
            longest_words.clear()
            longest_words.append(word[i])
            long_len = len(word[i])
        elif len(word[i]) == long_len:
            longest_words.append(word[i])
    
    return longest_words[0]

word = list(input("Enter a sentence: ").split())
print("Longest word: ", longest_word(word))
