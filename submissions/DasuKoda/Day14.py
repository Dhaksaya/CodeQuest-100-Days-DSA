def complete_str(s):
    result=s[0]
    for i in range(1,len(s)):
        if s[i]=='_':
            next_char= chr(ord(result[-1])+1)
            result+=next_char
        else:
            result+=s[i]
    return result
        
        
        



s="A_C_E"
print(complete_str(s))
        


"""
output 

ABCDE
"""