import numpy as np
f = open("input.txt", "r")

list1 = []
list2 = []
dict0 = {}

for line in f:
    line = line.strip()
    krneki = line.split()

    numb1 = int(krneki[0])
    numb2 = int(krneki[-1])
    list1.append(numb1)
    list2.append(numb2)
    if numb1 not in dict0:
        dict0[numb1] = 0

    if numb2 not in dict0:
        dict0[numb2] = 1
    else:
        dict0[numb2] += 1

result = 0
for i in list1:
    result += i*dict0[i]
print(result)
