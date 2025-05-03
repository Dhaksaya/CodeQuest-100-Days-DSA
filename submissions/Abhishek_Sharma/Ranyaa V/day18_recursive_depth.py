import ast
def find_depth(type):
    if not isinstance(type,list):
        return 0
    max_depth=1
    for i in type:
        if isinstance(i,list):
            max_depth= max(max_depth,1+find_depth(i))
    return max_depth
           

type=ast.literal_eval(input("enter a nested list:"))
result=find_depth(type)
print(f"The maze has a depth of {result}")