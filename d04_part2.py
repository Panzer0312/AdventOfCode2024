from utils.textinput import *
import numpy as np

word = "MAS"

def checkWords(w1,w2,w3,w4):
    count = 0
    if w1 == word:
        count +=1
    if w2 == word:
        count +=1
    if w3 == word:
        count +=1
    if w4 == word:
        count +=1
    if count == 2:
        return 1
    return 0

        # if y+c < len(field)+1 and x-c >= -1:
        #     lu += field[y+c-1][x-c+1]     
        # if y-c >= -1 and x-c >= -1:

def searchMAS(x,y,field):
    ru = ""
    rd = ""
    lu = ""
    ld = ""
    # print(x)
    for c in range(0,len(word)):
        if y+c < len(field)+1 and x+c < len(field[y])+1:
            ru += field[y+c-1][x+c-1]     
        if y-c >= -1 and x+c < len(field[y])+1:
            rd += field[y-c+1][x+c-1]  
        if y+c < len(field)+1 and x-c >= -1:
            lu += field[y+c-1][x-c+1]     
        if y-c >= -1 and x-c >= -1:
            ld += field[y-c+1][x-c+1]  
        # print(up,down)      
    print(ru)
    return checkWords(lu,ld,ru,rd)

def countXMAS(input):
    sum = 0
    for line in range(1,len(input)-1): 
        startingChars = [i for i, ltr in enumerate(input[line]) if ltr == "A"]
        for x in startingChars:
            if x > 0 and x < len(input[line]) -1:
                sum += searchMAS(x,line,input)
    return sum


file_path = '2024/input/d04_in.txt'
input = read_lines_from_file(file_path)
print(countXMAS(input))
