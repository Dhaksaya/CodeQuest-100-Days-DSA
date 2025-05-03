def longestword(sentence):
    words = sentence.split()
    maxlength = 0
    longest_word = ""
    for  word in words:
        if len(word) > maxlength:
            maxlength = len(word)
            longest_word = word
    print("Longest word: ",longest_word)
sentence = input("Enter a sentence: ")
longestword(sentence)