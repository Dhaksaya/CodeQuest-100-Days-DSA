n= str(input("Enter the secret message: "))
x=n.split()
reversed_wrds = [word[::-1] for word in x]
res=' '.join(reversed_wrds)
reversed_order = reversed_wrds[::-1] 
result=' '.join(reversed_order)
print(result)

