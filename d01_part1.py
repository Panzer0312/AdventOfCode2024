from utils.textinput import *
import numpy as np

def difference_list(a1,a2):
    diff = []
    for i in range(0,a1.size):
        diff.append(abs(a1[i]-a2[i]))
    return diff
            
def calculate_differences(arr):
    arr=np.array(arr)
    arr1,arr2= arr1,arr2=np.split(arr.astype(int),2,axis=1)
    arr1.shape = (arr1.size,)
    arr2.shape = (arr2.size,)

    arr1.sort()
    arr2.sort()    
    diff = difference_list(arr1,arr2)
    print(diff)
    sum = 0
    for i in diff:
        sum = sum + i
    return sum   

file_path = '2024/input/d01_in.txt'
input = read_lines_from_file(file_path,"   ")
print(calculate_differences(input))

