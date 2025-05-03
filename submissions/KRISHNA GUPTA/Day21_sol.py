n = list(map(int, input("Enter numbers: ").split()))
sum = 0
for i in range(len(n)):
    if (i+1) % 2 == 0:
       sum += n[i]
print("Hidden key:", sum)
