prime_num = int(input("Enter a number: "))

if prime_num >1:
    for num in range(2,int(prime_num**0.5)):
        if prime_num % num ==0:
            print("Not Prime")
        break
    else:
        print("Prime")