b=input("Enter binary number: ")
number=0
for i in b:
    number=number*2+int(i)   #as we have base '2' for binary, multiplying from MSB of the number can give the decimal equivalent
print('Decimal:',number)
