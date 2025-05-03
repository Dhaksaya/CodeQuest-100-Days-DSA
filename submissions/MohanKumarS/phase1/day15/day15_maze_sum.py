print("Enter numbers: ", end=' ')
numbers = list(map(int,input().split(' ')))
print("Secret Code: ",sum(numbers))