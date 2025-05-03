print("Note: After last number enter '-1'")
print("Enter numbers: ",end=" ")
decoded_message=[]
while(1):
    number=int(input())
    if (number>=0 and number<128):
        decoded_message.append(chr(number))
    else:
        break
print("Decoded message: ","".join(map(str,decoded_message)))
    