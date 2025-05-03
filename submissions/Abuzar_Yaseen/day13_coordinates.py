N = int(input("Enter N: "))
even = [digit for digit in str(N)
         if int(digit)%2 ==0]
if even :
        print("Even digits: "," ".join(even))
else:
        print("No even digits found! ")