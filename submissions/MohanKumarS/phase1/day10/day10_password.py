password = input("Enter your password: ")

# A-Z -> ASCII Value 65-90
# a-z -> ASCII Value 97-122

# upper is used to check whether there is a uppercase character in the password
# lower is used to check whether there is a lowercase character in the password
# digit is used to check whether there is a digits in the password
# specialCharacter is used to check whether there is a special character in the password
upper = lower = digit = specialCharacter = 0   #Initially assign all to zeros
alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" #to get non-alphabetic characters

for i in range(len(password)): # loop runs over the length of the password
    if password[i].isupper(): 
        upper = 1                        #if there is uppercase character in password, upper = 1
    elif password[i].islower():
        lower = 1                        #if there is lowercase character in password, lower = 1
    elif password[i].isdigit():
        digit = 1                        #if there is digit in password, digit = 1
    elif password[i] not in alphabets:
        specialCharacter = 1             #if the character is not in alphabets, then it is specialCharacter = 1
    #here digits are not check at the last elif, because if the digits are encountered the condition satisfied at the
    #second elif

if upper and lower and digit and specialCharacter and (len(password)>=8): 
    print("Strong Password") #if all the cases satisfied, it is Strong Password
else:
    print("Weak Password") #else Weak password

'''
constraints:
length -> len(password)>8
one uppercase -> 65 - 90
one lowercase -> 97 - 122
one number -> 0 - 9
one special character -> @, $, #
'''