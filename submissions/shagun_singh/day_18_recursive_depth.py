def find_depth(structure):
    if isinstance(structure, list):  # If it's a list, check inside
        return 1 + max((find_depth(item) for item in structure), default=0)
    return 0  # If it's not a list, return 0

# Taking user input as a simple string
nested_list = eval(input("Enter a nested list (e.g., [1, [2, [3, [4]]]]): "))

depth = find_depth(nested_list)
print(f"The maze has a depth of {depth}.")
