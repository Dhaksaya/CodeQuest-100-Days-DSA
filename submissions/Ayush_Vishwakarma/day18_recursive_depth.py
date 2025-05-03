# Recursive function to find the maximum depth of a nested list
def find_depth(lst):
    # Base case: if it's not a list, return 0
    if not isinstance(lst, list):
        return 0
    # If it's an empty list, depth is 1
    if not lst:
        return 1
    # Recursive case: 1 + max depth among all inner elements
    return 1 + max(find_depth(item) for item in lst)

# Input: Define your nested list here
maze = [1,[2,[3,4]]]

# Compute the depth
depth = find_depth(maze)

# Output the result
print(f"The maze has a depth of {depth}.")
