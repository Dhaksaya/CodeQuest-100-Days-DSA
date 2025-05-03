n=str(input("Enter string: "))
res=""
for i in range (len(n)):
    if n[i]=='_':
        pre_chr=n[i-1]
        nxt_chr=n[i+1]
        miss_chr=chr(ord(pre_chr)+1)
        res+=miss_chr
    else:
        res+=n[i]

print("Restored String:", res)