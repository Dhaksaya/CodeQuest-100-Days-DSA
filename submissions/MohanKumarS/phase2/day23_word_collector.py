def word_collector(word):
    # to get the clean word -> replace , . ! with ''
    cleaned_word = [w.replace(',', '').replace('.', '').replace('!', '').lower() for w in word]
    
    collector = {}
    for w in set(cleaned_word):  # count the unique word
        collector[w] = cleaned_word.count(w)
    
    # x -> each word
    for key in sorted(collector.keys(), key=lambda x: cleaned_word.index(x)): # sort based on the first appearance of the element in the cleaned_word
        print(f"{key}: {collector[key]}")

    return 0

word = input("Enter text: ").split(' ')
word_collector(word)
