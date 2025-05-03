k=list(input("ENTER"))#taking input from user
p=-1#initializing p to -1
for i in range(len(k)):#iterating through the input string
    if k[i]=='_':#if the character is an underscore
        if p!=-1:#if p is not -1
            k[i]=chr(p+1)
            p+=1
        else:#if p is -1
            pass##do nothing
    else:#if the character is not an underscore
        p=ord(k[i])#store the ASCII value of the character in p
print(" ".join(k))#printing the modified string with spaces between characters
