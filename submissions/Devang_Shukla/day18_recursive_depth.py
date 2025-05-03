def find_depth(structure):
    if not isinstance(structure,list):
        return 0
    stack = [(structure, 1)]
    max_depth =1
    while stack:
        current , depth = stack.pop()
        max_depth = max(max_depth,depth)
        for item in current:
            if isinstance(item,list):
                stack.append((item,depth + 1))
    return max_depth
            
# Input
maze = [1,[2,[3,[4]]]] 
depth = find_depth(maze)
print(f"The maze has a depth of {depth}.")   