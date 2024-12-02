import numpy as np
import math 
f = open("input.txt", "r")

goodRow = 0
oke = False
for line in f:
    intRow = line.split()
    
    intRow = [int(x) for x in intRow]
    predznak = np.sign(intRow[0]- intRow[1])
    for i in range(len(intRow)-1):
        temp = intRow[i]-intRow[i+1]
        if np.sign(temp)==predznak and abs(temp) <= 3 and abs(temp)>= 1:
            oke = True
        else: 
            oke = False
            break
    if oke:
        goodRow +=1
print(goodRow)
    
