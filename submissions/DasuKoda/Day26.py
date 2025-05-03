sentence=input("Enter the input sequance : ")
vowels="aeiouAEIOU"
v_count=0
c_count=0
for char in sentence:
    if char.isalpha():
        if char in vowels:
            v_count+=1
        else:
            c_count+=1
            
            
            
            
            
print("Vowels count",v_count)
print("consonanat count",c_count)





"""
Enter the input sequance : Hello World
Vowels count 3
consonanat count 7
"""