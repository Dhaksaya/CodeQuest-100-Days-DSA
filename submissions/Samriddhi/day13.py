#program to extract and print all even digits from a given number
n=int(input("Enter a number: "))
s=0
p=0
while n>0:
    r=n%10
    if r%2==0: #check if the digit is even
        s=s*10+r #store the even digit in reverse order
        p=1
    n=n//10 #remove the last digit from n
    


if p==1:#if even digits are found
    print("Even digits:", end=" ")#prints message if even digits are found
    while s>0:#reverse the order of even digits
      r=s%10#get the last digit of s
      print(r,end=" ")#print the even digit
      s=s//10
elif p==0:#if no even digits are found
    print("No even digits found")
# The above code extracts and prints all even digits from a given number.