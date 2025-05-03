def mystic_mirror(word): # used-defined function to find the vowels and consonants in word
    vowel_count = 0 # initialize the value as 0
    consonant_count = 0
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    
    for char in word: # traverse over the word
        if char in vowels: # if the letter is vowels, vowels_count gets incremented
            vowel_count += 1
        elif char in consonants: # if the letter is consonants, consonants_count gets incremented
            consonant_count += 1

    return vowel_count, consonant_count # return the values

word = input("Enter a sentence: ")
vowels, consonants = mystic_mirror(word.lower()) # positional assignments
print("Vowels:", vowels)
print("Consonants:", consonants)
