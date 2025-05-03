num = input("Enter N: ")
even_lst = []

for i in num:
    if  int(i) % 2 == 0:
        even_lst.append(i)

if even_lst:
    print("Even digits:", ' '.join(even_lst))
else:
    print("No even digits found!")
