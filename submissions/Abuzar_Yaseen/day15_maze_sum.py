maze = input("Enter numbers: ")
list_num = list(map(int,maze.split()))
total = sum(list_num)
print("Secret Code: ",total)
