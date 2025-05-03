num_find = input("Enter numbers: ")
num = list(map(int,num_find.split()))
total = 0
for even in range(len(num)):
    position =  even +1
    if position %2 == 0:
        total += num[even]
print("Hidden Key: ",total)

    