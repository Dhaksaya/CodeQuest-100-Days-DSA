 # type: ignore
string=input("Input: ")
start=ord(string[0])
end=ord(string[-1])
print("Output: ",end="")
for i in range(start,end+1): print(chr(i),end="")

