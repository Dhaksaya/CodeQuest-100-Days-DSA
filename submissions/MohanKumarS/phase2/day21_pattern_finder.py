n = list(map(int, input("Enter numbers: ").split(' ')))
sum = 0
for i in range(len(n)):
    if(i % 2 != 0):
        sum = sum + n[i]
print("Hidden Key: ", sum)