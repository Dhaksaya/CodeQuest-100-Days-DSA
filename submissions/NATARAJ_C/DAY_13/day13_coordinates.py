N=int(input("Enter N: "))
even=[]
for digit in str(N):
    if (int(digit)%2==0):
        even.append(int(digit))
if not even:
    print("No even digits found!")
else:
    print("Even digits: "," ".join(map(str,even)))