#Takes a list of integers as input (representing the maze wall numbers).
#Calculates the sum of these numbers.
#Prints the total sum, which represents the secret code  
# Taking user input and converting it into a list of integers
maze_input=int(input("ENTER NUMBERS "))
SUM=0
while maze_input>0:
    digit=maze_input%10
    SUM+=digit
    maze_input//=10
print("the sum of digits : ",SUM)    
