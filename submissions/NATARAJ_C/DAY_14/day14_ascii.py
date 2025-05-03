string=input("Enter string: ")
restored_string=[]
for i in string:
    if(ord(i)>96):
        restored_string.append(i)
    elif(ord(i)==95):
        if not restored_string:
           restored_string.append(chr(ord(string[1])-1)) #if 1st element is missing
        else:
            i=chr(ord(restored_string[-1])+1)
            restored_string.append(i)
print("Restored string: ","".join(map(str,restored_string)))