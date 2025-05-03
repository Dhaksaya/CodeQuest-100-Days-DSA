n=int(input("Enter a Number : "))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")
    
    """
    
    
    Enter a Number : 5
Prime


   Enter a Number : 10
Not Prime
 
    
    
    
    
    
    """