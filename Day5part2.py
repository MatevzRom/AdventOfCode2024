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
    flag = False
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
            flag = True
            break
    if flag:
        # Repair
        generative = []
        dodatek = []
        # print(generative)
        generative.append(row[0])
        quickfix = 0
        for num1 in row:
            if quickfix == 0:
                quickfix+=1
                continue
            # print(num1)
            mesto = 0
            ff = True
            for i in range(len(generative)):
                print(generative)
                # print("mjau")
                
                # if generative == []:
                #     generative.append(num1)
                #     print("tuki")
                if num1 not in dic:
                    if num1 not in dodatek:
                        # print("tukiii")
                        dodatek.append(num1)
                    break
                elif generative[i] in dic[num1]:
                    # if i == len(generative)-1:
                    #     generative.append(num1)
                    mesto = i+1
                # else:
                #     generative.insert(i,num1)
            if mesto != -1:
                generative.insert(mesto,num1)
            
            # print(dodatek)
        dodatek.reverse()
        kk = generative
        print(kk)
        # print("---")

        

        # add sum
        result += kk[int((len(kk)-1)/2)]
        # print(kk[int((len(kk)-1)/2)])
print(result)