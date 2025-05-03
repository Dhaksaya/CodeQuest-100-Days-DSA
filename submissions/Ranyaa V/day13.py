N = input("Enter N: ")

# Use filter to keep even digits only
even_digits = list(filter(lambda d: d.isdigit() and int(d) % 2 == 0, N))

if even_digits:
    print("Even digits:", ",".join(even_digits))
else:
    print("No even digits found!")
