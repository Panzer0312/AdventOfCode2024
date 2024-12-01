from utils.textinput import *
import numpy as np

def difference_list(a1,a2):
    unique, counts = np.unique(a2, return_counts=True)
    occ = dict(zip(unique,counts))
    diff = []
    for i in a1:
        if i in occ:
            diff.append(i*occ[i])
        else:
            diff.append(0)
    return diff       

def calculate_similarities(arr):
    arr=np.array(arr)
    arr1,arr2= arr1,arr2=np.split(arr.astype(int),2,axis=1)
    arr1.shape = (arr1.size,)
    arr2.shape = (arr2.size,)
    diff = difference_list(arr1,arr2)
    sum = 0
    for i in diff:
        sum = sum + i
    return sum   

file_path = '2024/input/d01_in.txt'
input = read_lines_from_file(file_path,"   ")
print(calculate_similarities(input))

