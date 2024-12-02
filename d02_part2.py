from utils.textinput import *
import numpy as np

def test_delete(row,point):
    new_row = np.delete(row,point)
    return check_row_safety(new_row)

def stage_deletable(row):
    for i in range(0,len(row)):
       if test_delete(row,i):
           return True
    return False

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
        arr=np.array(i).astype(int)
        if check_row_safety(arr):
            safe_rows +=1
        else:
            if stage_deletable(arr):
                safe_rows +=1
    return safe_rows


file_path = '2024/input/d02_in.txt'
input = read_lines_from_file(file_path," ")
print(check_list_safety(input))
