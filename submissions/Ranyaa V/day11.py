input_str=input("enter numbers")
numbers=list(map(int,input_str.strip().split()))
numbers.sort()
print(numbers)