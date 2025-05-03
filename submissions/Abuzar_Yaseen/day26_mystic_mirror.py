def vowels_consonants(sentence):
    sentence = sentence.lower()
    vowel_count =0
    consonant_count = 0
    vowels = 'aeiou'
    for char in sentence:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    print("Vowels: ",vowel_count)
    print("Consonants: ",consonant_count)

sentence = input("Enter a sentence: ")
vowels_consonants(sentence)
