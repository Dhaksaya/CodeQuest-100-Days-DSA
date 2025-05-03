sentence=input("Enter a sentence: ")
words=sorted((sentence.split()),key=len)
print("Longest word:",words[-1])


