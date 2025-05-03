num=int(input("Enter a num: "))
fact=1
if num>=0:
    if num==0 or num==1: fact=1
    else:
        for i in range(1,num+1): fact*=i
    print(f"Factorial of {num} is {fact}")
else: print("Enter a positive number.")
