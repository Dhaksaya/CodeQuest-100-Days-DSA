numbers_1=input("Enter first list: ")
numbers_2=input("Enter second list: ")
list1=list((map(int,numbers_1.split())))
list2=list((map(int,numbers_2.split())))
set1=set(list1)
set2=set(list2)

common=set1 & set2  #using set property to find the overlapping elements

if common:
    print("Common elements:",*common)  #using '*' symbol, to remove the curly bracers or to print only integers of the set
else:
    print("No common elements found!")