a=input('Enter numbers: ').split() #receices the input as string and splits it
a=[int(i) for i in a]              #used type casting to convert from string to int
print("Secret Code: ",sum(a))      #printing result..