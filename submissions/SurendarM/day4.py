a=input('Enter a number: ')
print("sum of digits: ")
b=[int(i) for i in a]
for i in range(len(b)):
    print(b[i],'+',end='') if(i!=len(b)-1) else print(b[i],end='')
print('=',sum(b))