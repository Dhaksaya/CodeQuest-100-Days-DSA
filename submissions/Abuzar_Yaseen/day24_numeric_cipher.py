decode = input("Enter numbers: ")
numbers = decode.split()
characters = [chr(int(num)) for num in  numbers]
message = "".join(characters)
print("Decoded message: ",message)