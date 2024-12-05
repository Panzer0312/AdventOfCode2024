from utils.textinput import *
import numpy as np

word = "XMAS"

def checkWords(w1,w2):
    count = 0
    if w1 == word:
        count +=1
    if w2 == word:
        count +=1
    return count

def searchHorizontal(x, line):
    count = 0
    right = ""
    left = ""
    for c in range(0,len(word)):
        if x+c < len(line):
            left += line[x+c]     
        if x-c >= 0:
            right += line[x-c]
        # print(left,right)
    return checkWords(right,left)

def searchVertical(x,y,field):
    count = 0
    up = ""
    down = ""
    for c in range(0,len(word)):
        if y+c < len(field):
            up += field[y+c][x]     
        if y-c >= 0:
            down += field[y-c][x]  
        print(up,down)
    return checkWords(up,down)
    
def searchDiagonal(x,y,field):
    ru = ""
    rd = ""
    lu = ""
    ld = ""
    
    for c in range(0,len(word)):
        if y+c < len(field) and x+c < len(field[x]):
            ru += field[y+c][x+c]     
        if y-c >= 0 and x+c < len(field[x]):
            rd += field[y-c][x+c]  
        if y+c < len(field) and x-c >= 0:
            lu += field[y+c][x-c]     
        if y-c >= 0 and x-c >= 0:
            ld += field[y-c][x-c]  
        # print(up,down)      
    
    return checkWords(ru,rd) + checkWords(lu,ld)

def searchXMAS(x,y,field):
    found = 0
    found += searchHorizontal(x,field[y])
    found += searchVertical(x,y,field)
    found += searchDiagonal(x,y,field)
    return found


def countXMAS(input):
    sum = 0
    for line in range(0,len(input)):
        startingChars = [i for i, ltr in enumerate(input[line]) if ltr == word[0]]
        for x in startingChars:
           sum += searchXMAS(x,line,input)
    return sum


file_path = '2024/input/d04_in.txt'
input = read_lines_from_file(file_path)
print(countXMAS(input))
