import re
password=input("Enter your password: ")
errors=[]
if len(password) <=8 :
    print("Weak Password (Password should be atleast 8 characters)")
if not any(char.isupper() for char in password):
        errors.append("a uppercase character")
if not any(char.islower() for char in password):
        errors.append("a lowercase character")
if not any(char.isdigit() for char in password):
        errors.append("a number")
if not re.search(r"[!@#$%^&*(),.?\:{}|<>]",password):
        errors.append("a special character")
if errors:
    print(f"Weak Password Missing ({' and '.join(errors)}) ")
else: print("Strong password")