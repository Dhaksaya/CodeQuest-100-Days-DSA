n=input("Enter N : ")
vundi=False
for i in n:
    if (i.isdigit()):
        if(int(i)%2==0):
            print(i,end=' ')
            vundi=True
if not vundi:
    print("No even digit found !")
    
    
    
    """
    Enter N : 12345678
    2 4 6 8 
    
    Enter N : 13579
    No even digit found !

    
    """