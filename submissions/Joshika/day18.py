def find_depth(my_list):
    max_depth = 1
    for item in my_list:
        if type(item) == list:
            depth = 1 + find_depth(item)
            if depth > max_depth:
                max_depth = depth
    return max_depth
text = input("Type a list: ")
my_list = eval(text)
result = find_depth(my_list)
print("The maze has a depth of", result)
 