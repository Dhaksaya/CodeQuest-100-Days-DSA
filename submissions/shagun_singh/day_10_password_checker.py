#Takes a password as input
#Checks if it meets all the strength requirements
#Prints “Strong Password” or “Weak Password”
#A password is considered strong if:
#✅ It has at least 8 characters
#✅ It contains at least one uppercase letter (A-Z)
#✅ It contains at least one lowercase letter (a-z)
#✅ It contains at least one digit (0-9)
#✅ It contains at least one special character (like @, #, $, etc.)
import string 
def password_checker(password):
    if len(password)<8:
        return "WEAK PASSWORD"
    if not any(char.isupper() for char in password):
        return "WEAK PASSWORD"
    if not any(char.islower() for char in password):
       return "WEAK PASSWORD"
    if not any(char.isdigit() for char in password):
        return "WEAK PASSWORD" 
    special_characters=string.punctuation
    if not any(char in special_characters for char in password):
        return "WEAK PASSWORD"
    #if all conditions are true
    return "STRONG PASSWORD"             
password=input("ENTER YOUR PASSWORD :")
print(password_checker(password))
 
