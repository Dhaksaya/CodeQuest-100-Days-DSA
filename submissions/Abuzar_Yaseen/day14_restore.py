def restored(string):
    result= list(string)
    for i in range(1,len(result)):
        if string[i] == "_":
            result[i] = chr(ord(result[i-1])+1)
    return ''.join(result)

input_string1= restored("a_c_e")
input_string2 = restored("m_no_q")
print("Restored string: ",input_string1)
print("Restored string: ",input_string2)