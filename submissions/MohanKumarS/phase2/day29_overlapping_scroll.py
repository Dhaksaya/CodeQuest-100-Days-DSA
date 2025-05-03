def overlapping_scroll(lst1, lst2):
    lst1 = [int(i) for i in lst1]
    lst2 = [int(i) for i in lst2]

    common_elements = list(set(lst1) & set(lst2))

    if len(common_elements) == 0:
        return None  
    return common_elements

lst1 = list(input("Enter first list: ").split())
lst2 = list(input("Enter second list: ").split())
common_elements = overlapping_scroll(lst1, lst2)
if common_elements is None:
    print("No common elements found!")
else:
    print("Common elements: ", ' '.join(str(i) for i in common_elements)) # join() works only with strings