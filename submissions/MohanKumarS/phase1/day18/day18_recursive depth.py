# Recursive function: find the depth of the nested list
def find_depth(lst):
    if not isinstance(lst, list):
        return 0
    elif not lst:
        return 1
    else:
        return 1 + max(find_depth(item) for item in lst)

# to get the nested list as input from the user
import ast

maze = input("Enter a nested list: ")
try:
    maze = ast.literal_eval(maze)
except Exception as e:
    print("Invalid input:", e)


depth = find_depth(maze) # function call
print(f"The maze has a depth of {depth}.") # use of format function

"""
The ast module in Python stands for Abstract Syntax Tree. 
It is a built-in module that helps you interact with Python code structures and 
  parse Python source code into its abstract syntax tree (AST) representation.
ast.literal eval(): Because it safely evaluates the input string as a Python literal (like list, dict, tuple, etc.)
                    without running arbitrary code like eval() does.
"""