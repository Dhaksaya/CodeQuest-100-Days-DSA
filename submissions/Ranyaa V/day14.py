def restore_string(s):
    result=list(s)
    for i in range(1,len(result)):
        if result[i]=='_':
            result[i]=chr(ord(result[i-1])+1)
    return ''.join(result)
    
print(restore_string("a_c_e"))
print(restore_string("m_no_q"))