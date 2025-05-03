import string
n=input("Enter your password: ")
is_uppercase = False
is_lowercase = False
is_digit_avble = False
is_spcl_chrcter = False

if len(n)>=8 :
    for i in n:
        if i.isupper():
            is_uppercase = True
        elif i.islower():
            is_lowercase = True
        elif i.isdigit():
            is_digit_avble = True
        elif i in string.punctuation:
            is_spcl_chrcter = True
        
    if is_uppercase and is_lowercase and is_digit_avble and is_spcl_chrcter:
        print("Strong Password")
    else:
        print("Weak Password (Missing uppercase letter and special character)")



