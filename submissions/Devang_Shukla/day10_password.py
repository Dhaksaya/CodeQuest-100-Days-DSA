import string

# Day 10 - password strength checker

# Take password input
password = input("Enter your password: ")

#  Initialize flagg
has_upper = False
has_lower = False
has_digits = False
has_special = False

# Check password length
if len(password) >= 8:
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digits = True
        elif char in string.punctuation:
            has_special = True

    # Final evaluation
    if has_upper and has_lower and has_digits and has_special:
        print("Strong Password")
    else:
        print("Week Password (Missing:",end=',')
        if not has_upper:
            print("uppercase letter",end=',')
        if not has_upper:
            print("lowercase letter",end=',')
        if not has_digits:
            print("Digits",end=',')
        if not has_special:
            print("special character",end='')
        print(")")
else:
    print("Weak Password (Minimum length should be 8 characters)")                
    
