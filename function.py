import numpy as np

def compare(a, b):
    """
    Compare 2 integer
    Input: 
        Int a
        Int b
    Output:
        True or False
    If a > b then return True
    else if a < b then return False
    """
    if a > b :
        return True
    else :
        return False
    
def read_file(str):
    """
    Read array from file (with filename is str)
    Input: 
        string str: text file name
    Output:
        array arr: Array reading from text file"""
    arr = np.loadtxt(str, dtype=int, delimiter=',')
    return(arr)

def swap(a, m ,n):
    """ Swap m and n position in array a
    Input:
        a: array
        m: position m
        m: position n
    Output:
        a: array after swap
        
        The first position in array is index 0
    """
    temp = a[m]
    a[m] = a[n]
    a[n] = temp
    
    return a

def write_file():
    arr = np.array(np.random.permutation(10000))
    np.savetxt("my_array_10000.txt", arr, fmt='%d', delimiter=',')

    arr1 = np.array(np.random.permutation(10))
    np.savetxt("my_array_10.txt", arr1, fmt='%d', delimiter=',')