def main(list):#input of a list
    m=1#initializing m to 1
    for item in list:#iterating through the list
        if isinstance(item, list):#checking if the item is a list
            d=1+main(item)#recursive call to main function
            m=max(m,d)#updating m to the maximum of m and d
    
    return m#returning m


