def extract_even_digits(N):
    even_digits = [digit for digit in str(N) if int(digit) % 2 == 0]
    
    if even_digits:
        print("Even digits:", "".join(even_digits))
    else:
        print("No even digits found!")
        
# Example usage
N = input("Enter a number: ")
extract_even_digits(N)
