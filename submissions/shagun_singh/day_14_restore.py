def restore_string(s):
    result = []
    for i in range(len(s)):
        if s[i] == '_':  
            missing_char = chr(ord(s[i-1]) + 1)
            result.append(missing_char)
        else:
            result.append(s[i])
    
    return "".join(result)

# Example usage
input_string = "A_B_C_D"
output_string = restore_string(input_string)
print(output_string)
