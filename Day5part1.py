import numpy as np
f = open("input.txt", "r")
rrow = [75,47,61,53,29]
arr = []
firstPart = True
dic = {}
input = []
for line in f:
    line = line.strip()
    if(line == ""):
        firstPart = False
        continue
    if firstPart:
        row_numbers = line.strip().split("|")
        row_numbers = [int(a) for a in row_numbers]
        first = row_numbers[0]
        if first in dic:
            dic[first].append(row_numbers[1])
        else:
            dic[first] = [row_numbers[1]]
        # if row_numbers[]
        # dict[row_numbers[0]].append
    else:
        input.append([int(a) for a in line.strip().split(",")])
# print(dic)
# print(input)
result = 0

for row in input:
    # row = rrow
    
    row.reverse()
    # print(row)
    flag = True
    before = []
    generative = []
    for numb in row:
        # print(numb)
        if numb not in before:
            generative.append(numb)
            if numb in dic:
                before += dic[numb]
            # print(generative)
            # print(before)
            # print("---")
        else:
            flag = False
            break
    if flag:
        result += row[int((len(row)-1)/2)]
print(result)


