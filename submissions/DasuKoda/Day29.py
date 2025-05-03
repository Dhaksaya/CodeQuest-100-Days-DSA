list1=list(map(int,input("Enter the input sequance : ").split()))
list2=list(map(int,input("Enter the input sequance : ").split()))
common=list(set(list1) & set(list2))
if common:
    print("The common is : ", common)
else:
    print("No Common ")
    
    
  """  
    Enter the input sequance : 1 2 3 4 5
Enter the input sequance : 4 5 6 7 8
The common is :  [4, 5]

=== Code Execution Successful ===
"""