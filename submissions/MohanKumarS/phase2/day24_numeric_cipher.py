def numeric_cipher(numbers): # user-defined function -> to convert the numbers into ASCII character
    for i in range (len(numbers)):
        numbers[i] = chr(int(numbers[i])) # convert each numbers into corresponding ASCII using chr() function
    return ''.join(numbers) # join() is used to convert list into a string


numbers = list(input("Enter numbers: ").split(' '))
print("Decoded Message: ", numeric_cipher(numbers))