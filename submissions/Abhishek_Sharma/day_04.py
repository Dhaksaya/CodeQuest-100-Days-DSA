number=input("Enter a number:- \n")
digits = []
sum=0
for i in number:
    digits.append(i)
    sum += int(i)
expression = " + " .join(digits)
print(f"Sum of digits: {expression} = {sum}")

number = input("Enter a number:- \n")
sum = 0
expression = ""

for i in number:
    sum += int(i)  # Calculating the sum of digits
    if expression:  # If it's not the first digit, add " + " before the number
        expression += " + "
    expression += i  # Adding the current digit to the expression

print(f"Sum of digits: {expression} = {sum}")
