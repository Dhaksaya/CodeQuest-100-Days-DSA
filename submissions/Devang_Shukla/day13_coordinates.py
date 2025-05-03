#Day 13 - Extract Even Digits from a Number

# Take input from the user 
N = input("Enter N:")

#List to store even digit 
even_digit = []

#Iterate through each digit in the number 
for digit in N:
   if digit.isdigit() and int(digit) % 2 == 0:
      even_digit.append(digit)

# Print result based on whether any even digit were found
if even_digit:
   print("Even digit:",' '.join(even_digit))
else:
    print("No even digit found!")     