from function import *

arr = read_file("my_array_10.txt")
length = len(arr)
print(arr)

for i in range(0, length):
    min = i
    for j in range(i+1,length):
        if (arr[j] < arr[min]):
            min = j
    arr = swap(arr, i, min)
    
print(arr)