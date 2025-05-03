data = eval(input())
depth = 0
stack = [(data, 1)] 
while stack:
    element, current_depth = stack.pop()
    if isinstance(element, list):
        if current_depth > depth:
            depth = current_depth
        for item in element:
            stack.append((item, current_depth + 1))
print("The maze has a depth of", depth, end=".")