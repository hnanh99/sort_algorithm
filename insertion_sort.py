from function import *

arr = read_file("my_array_10.txt")
length = len(arr)
print(arr)
for i in range(0,length):
    key = arr[i]
    j = i
    while ((j > 0) & (arr[j-1] > key)):
        arr[j] = arr[j-1]
        j = j - 1
    arr[j] = key

print(arr)