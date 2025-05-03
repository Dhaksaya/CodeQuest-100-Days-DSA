def binary_to_decimal(binary):  # user-defined function -> to convert binary to decimal
   if not all(ch in '01' for ch in binary): # check whether the number is binary or not
     print("Error: Enter a valid binary number (only 0s and 1s).")
     return None # if not return None
   
   decimal = 0
   for i, ch in enumerate(binary[::-1]): # enumerate -> get the index and value at same time -> i=index; ch = value
       decimal = decimal + int(ch)*(2 ** i) # decimal conversion logic
   return decimal

binary = input("Enter binary number: ")
decimal = binary_to_decimal(binary) # function call

if decimal is not None: # it prints the result if and only if decimal is not None
   print("Decimal: ", decimal)