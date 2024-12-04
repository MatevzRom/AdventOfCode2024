import numpy as np
f = open("input.txt", "r")
arr = []
for line in f:
    line = line.strip()
    arr.append(list(line))


arr = np.array(arr)
# print(arr)
vsota = 0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i,j]=="A":
            # Border pogoji
            if i-1 >=0 and j-1>=0 and i+1<len(arr) and j+1<len(arr[0]):
                # matching crke pogoji major diagonal
                if (arr[i-1,j-1]=="M" and arr[i+1,j+1]=="S") or (arr[i-1,j-1]=="S" and arr[i+1,j+1]=="M"):
                    # matching crke pogoji minor diagonal
                    if (arr[i-1,j+1]=="M" and arr[i+1,j-1]=="S") or (arr[i-1,j+1]=="S" and arr[i+1,j-1]=="M"):
                        vsota+=1
print(vsota)
