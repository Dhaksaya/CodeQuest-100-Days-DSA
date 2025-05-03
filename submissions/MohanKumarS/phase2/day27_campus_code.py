def campus_code(lst):
    modules = [] # module list -> used to store the values below the threshold level
    for i in range(len(lst)):
        if(int(lst[i]) < 50): # the lst values are of type string, by explicitly convert it into int by using int()
            modules.append(lst[i]) # if the value below 50, it gets append in the module list
    if len(modules) == 0: # if len(modules) == 0, denotes none of the values are below 50. Hence return None for indication
        return None
    return modules

lst = list(input("Enter module scores (space-separated): ").split())
modules = campus_code(lst) # called the function campus_code(lst) with arguments 'lst'
if modules is None: # if the module is None, then all modules working fine
    print("All modules are working fine!")
else:
    print("Modules to debug: ", ' '.join(modules)) # ' '.join() -> it converts list into string
