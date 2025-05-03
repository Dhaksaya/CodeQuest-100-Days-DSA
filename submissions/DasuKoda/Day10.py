import re
def is_strong(password):
    if len(password)<8:
        return False
    if not re.search(r'[A-Z]',password):
        return False
    if not re.search(r'[a-z]',password):
        return False
    if not re.search(r'[0-9]',password):
        return False
    if not re.search(r'[@#%^&*()!~:<>?"]',password):
        return False
    return True




p=input("Enter Your password :")
if(is_strong(p)):
    print("Strong Password")
else:
    print("Weak Password (Missing uppercase letter and special character)")
