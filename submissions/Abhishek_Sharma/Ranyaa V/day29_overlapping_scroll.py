
l1=list(map(int,input("Enter first list: ").split()))
l2=list(map(int,input("Enter second list:").split()))
s1=set(l1)
s2=set(l2)
common=s1.intersection(s2)
l3=list(common)
s3=" ".join(map(str,l3))
if common:
    print(f"Common elements:{s3}")
else:
    print("No common elements found!")