text=input("Enter the sentence : ")
words=text.lower().split()
word_count={}
for word in words:
    word_count[word]=word_count.get(word,0)+1
     
for word,count in word_count.items():
    print(word, ":", count)
    
    """
    Enter the sentence : The Glitch is everywhere and the Glitch never sleeps.
the : 2
glitch : 2
is : 1
everywhere : 1
and : 1
never : 1
sleeps. : 1

    """
     
