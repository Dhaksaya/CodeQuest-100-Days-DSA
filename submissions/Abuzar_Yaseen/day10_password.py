import string
def secure_password(password):
    if(len(password) < 8):
        return False
    is_upper = False
    is_lower = False
    is_digit = False
    is_special = False
    for letter in password:
        if letter.isupper():
            is_upper = True
        elif letter.islower():
            is_lower = True
        elif letter.isdigit():
            is_digit = True
        elif letter in string.punctuation:
            is_special = True
    return is_upper and is_lower and is_digit and is_special
password = input("Enter your passord: ")
if secure_password(password):
    print("Strong Password")
else:
    print("Weak Password (Missing uppercase letter and special character)")
