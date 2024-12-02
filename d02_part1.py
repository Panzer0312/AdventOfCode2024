from utils.textinput import *
import numpy as np


def check_row_safety(row):
    diff = 0
    for i in range(1,len(row)):
        new_diff = row[i-1] - row[i]
        if abs(new_diff) < 1 or abs(new_diff) > 3:
            return False
        
        if diff * new_diff < 0:
            return False        
        diff = new_diff
    return True
        
        

def check_list_safety(input):
    safe_rows = 0
    for i in input:
        arr=np.array(i)
        if check_row_safety(arr.astype(int)):
            safe_rows +=1

    return safe_rows


file_path = '2024/input/d02_in.txt'
input = read_lines_from_file(file_path," ")
print(check_list_safety(input))
