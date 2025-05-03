def bubbleSort(lst):  # Bubble sort -> swap two consecutive elements if the 1st element greater than 2nd element
    for i in range (len(lst)):
        for j in range(len(lst)-i-1):
            if(lst[j] > lst[j+1]):
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
    return lst

def insertionSort(lst): # Insertion sort
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j = j - 1
            print(lst)
        lst[j+1] = key
    return lst

lst = list(map(int, input("Enter numbers: ").split(' ')))
print("Sorted Data: ", bubbleSort(lst))
print("Sorted Data: ", insertionSort(lst))
