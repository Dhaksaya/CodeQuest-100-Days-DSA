N = input("Enter N: ")
a = 0 # used to know whether the enter number has a even digits or not
one_iterate = True

for i in N:
    if(int(i)%2 == 0):
        if(one_iterate): # this conditional block is used to print 'Even digits: ' only one time, if there is a even digit
            print("Even digits: ",end='')
            one_iterate = False
        print(int(i), end=' ')
        a = 1 # if the entered number has even digit, 'a' is assigned to 1
if(a == 0): # if the value of 'a' remains in 0, indicates there is no even digits in the enter number
    print("No even digits found!")