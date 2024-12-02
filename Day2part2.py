import numpy as np
import math 

def checkSafety(intRow):
    oke = False
    predznak = np.sign(intRow[0]- intRow[1])
    for i in range(len(intRow)-1):
        temp = intRow[i]-intRow[i+1]
        if np.sign(temp)==predznak and abs(temp) <= 3 and abs(temp)>= 1:
            oke = True
        else: 
            oke = False
            break
    return oke

f = open("input.txt", "r")
goodRow = 0

for line in f:
    intRow = line.split()
    intRow = [int(x) for x in intRow]
    
    if checkSafety(intRow):
        goodRow+=1
    else:
        for i in range(len(intRow)):
            copyArray = intRow.copy()
            copyArray.pop(i)
            if checkSafety(copyArray):
                goodRow+=1
                break
print(goodRow)
        
