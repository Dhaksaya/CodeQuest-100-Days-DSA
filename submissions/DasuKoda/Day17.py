def find_depth(struct):
    if not isinstance(struct,list):
        return 0
    elif not struct:
        return 1
    else:
        return 1+max(find_depth(item) for item in struct)
     
     
     
     
maze=[[[[]]]];
depth=find_depth(maze)
print("the depth of maze is :", depth)



"""

the depth of maze is : 4

"""