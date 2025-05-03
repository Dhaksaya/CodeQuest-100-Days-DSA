def find_depth(structure):
    if not isinstance(structure, list):
        return 0
    elif not structure:
        return 1
    else:
        return 1 + max(find_depth(item) for item in structure)

# Example
s =input("Input: ")
maze = eval(s)
depth = find_depth(maze)
print(f"The maze has a depth of {depth}.")