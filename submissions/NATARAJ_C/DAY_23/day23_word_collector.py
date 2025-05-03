t=input("Enter text: ")
list1=(t.lower()).split()
for word in set(list1):
    print(f"{word}: {list1.count(word)}")




