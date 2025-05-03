import string
password=input("enter your password")
has_upper=any(c.isupper() for c in password)
has_lower=any(c.islower() for c in password)
has_digit=any(c.isdigit() for c in password)
has_special=any(c in string.punctuation for c in password)
if len(password)>=8 and has_digit and has_upper and has_lower and has_special:
    print("strong password")
else:
    print("weak password" )