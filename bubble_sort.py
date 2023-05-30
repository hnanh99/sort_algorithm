"""Bubble Sort
"""

from function import *


arr = read_file("my_array_10.txt")
print(arr)
for i in range(0,len(arr)):
    for i in range(0,len(arr)-1):
        if arr[i] > arr[i+1]:  
            swap(arr,i,i+1)
        
print(arr)