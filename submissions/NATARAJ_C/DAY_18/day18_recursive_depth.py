def count_mazes(nested_list):
    maze_count=0
    if not nested_list:
        return maze_count
    for item in nested_list:
        if isinstance(item,list):
            maze_count+=1
            maze_count+=count_mazes(item)
    return maze_count

import ast
list_input=input("Enter a nested list: ")
try:
    nested_list = ast.literal_eval(list_input)
    if not isinstance(nested_list, list):
        raise ValueError("Input must be a list.")
except (ValueError, SyntaxError):
    exit()


print("The maze has a depth of",(count_mazes(nested_list)+1))