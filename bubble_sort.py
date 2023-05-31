"""Bubble Sort
"""

from function import *


arr = read_file("my_array_10000.txt")
print(arr)
length = len(arr)
for i in range(0,length):
    for i in range(0,length-1):
        if arr[i] > arr[i+1]:  
            swap(arr,i,i+1)
        
print(arr)