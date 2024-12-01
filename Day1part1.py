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

list1.sort()
list2.sort()

list1 = np.array(list1)
list2 = np.array(list2)

test = abs(list1-list2)

print(sum(test))