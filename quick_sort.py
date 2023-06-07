from function import *
arr = read_file("my_array_10.txt")

# def Quick_Sort(arr):
"""Quick Sort"""
#     less = []
#     equal = []
#     bigger = []
    
#     if len(arr) > 1:
        
#         pivot = arr[0] #pivot là đặt trưng của quicksort
        
#         for x in arr:
#             if x < pivot:
#                 less.append(x)
#             if x == pivot: 
#                 equal.append(x)
#             if x > pivot:
#                 bigger.append(x)
#         return Quick_Sort(less) + equal + Quick_Sort(bigger)
#     else:
#         return arr

def qsort(arr):
    """Quick Sort from Stackoverflow"""
    if len(arr) <= 1:
        return arr
    else:
        return qsort([x for x in arr[1:] if x < arr[0]]) + [arr[0]] + qsort([x for x in arr[1:] if x >= arr[0]])
print(arr)        
arr = qsort(arr)
print(arr)