user_pass = input("Enter your password: ")

upper_check = lower_check = digit_check = special_char_check = False
missing = []

if len(user_pass) >= 8:
    for char in user_pass:
        if char.isupper():
            upper_check = True
        if char.islower():
            lower_check = True
        if char.isdigit():
            digit_check = True
        if not char.isalnum():
            special_char_check = True

    if not upper_check:
        missing.append("uppercase letter")
    if not lower_check:
        missing.append("lowercase letter")
    if not digit_check:
        missing.append("digit")
    if not special_char_check:
        missing.append("special character")

    if missing:
        print(f"Weak Password (Missing {', '.join(missing)})")
    else:
        print("Strong password")

else:
    print("Weak Password (Must be at least 8 characters long)")
