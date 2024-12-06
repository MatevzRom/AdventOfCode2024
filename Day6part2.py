import numpy as np
import copy
class Guard:
    def __init__(self, direction, position):
        self.direction = direction
        self.position = position
    def __str__(self):
        return "Direction: "+str(self.direction)+", position: "+str(self.position)
    def turn(self):
        if self.direction == "^":
            self.direction = ">"
        elif self.direction == ">":
            self.direction = "v"
        elif self.direction == "v":
            self.direction = "<"
        elif self.direction == "<":
            self.direction = "^"
        else: print("SELF DIRECTION WAS NOT VALID OPTION")
    def copy(self):
        copy = Guard(self.direction,self.position)
        return copy
# ^><v
def krneki (guard,mapa,test, globina):
    vsota = 0
    while True:
        # ^
        if guard.direction == "^":
            i,j = guard.position
            if i == 0:
                mapa[i,j] ="X"
                # print("stepping out")
                break
            elif mapa[i-1,j] != "#":
                if globina == 0 and '#' not in test[i-1][j]:
                    copyGuard = guard.copy()
                    copyMapa = np.copy(mapa)
                    copyTest = copy.deepcopy(test)
                    copyMapa[i-1,j] = '#'
                    vsota+= krneki(copyGuard,copyMapa,copyTest,1)
                    test[i-1][j]+='#'
                    # globina=1


                if "^" in test[i-1][j]:
                    # print(str(i-1)+" "+str(j))
                    # print("CIKEL1")
                    # print(mapa)
                    return 1
                # print("cando")
                guard.position=(i-1,j)
                mapa[i,j] = "X"
                
                mapa[i-1,j] = guard.direction
                test[i][j] += guard.direction
                # test[i-1][j] += guard.direction
                # print(mapa[i,j])
                #ce je x sosed razn iz smeri kjer si prsu:
                
            elif mapa[i-1,j] == "#":
                test[i][j] += guard.direction
                guard.turn()
                mapa[i,j]= guard.direction
                
            else:
                print("Error, impossible condition")
                break
        # >
        if guard.direction == ">":
            i,j = guard.position
            if j == len(mapa[0])-1:
                mapa[i,j] ="X"
                # print("stepping out")
                break
            elif mapa[i,j+1] != "#":
                if globina == 0 and '#' not in test[i][j+1]:
                    copyGuard = guard.copy()
                    copyMapa = np.copy(mapa)
                    copyTest = copy.deepcopy(test)
                    copyMapa[i,j+1] = '#'
                    vsota+= krneki(copyGuard,copyMapa,copyTest,1)
                    test[i][j+1] += '#'
                if ">" in test[i][j+1]:
                    # print(str(i)+" "+str(j+1))
                    # print("CIKEL2")
                    # print(mapa)
                    # for row in test:
                    #     print(row)
                    return 1
                tempI = i
                
                # print("cando")
                guard.position=(i,j+1)
                mapa[i,j] = "X"
                mapa[i,j+1] = guard.direction
                test[i][j] += guard.direction
                # test[i][j+1] += guard.direction
                # print(mapa[i,j])
                j=j+1
                # if (j+1 != len(mapa)-1 and mapa[i,j+1]=='X'):
                #     count+=1
                #     print(mapa)
                #     print("tuki")
            elif mapa[i,j+1] == "#":
                test[i][j] += guard.direction
                guard.turn()
                mapa[i,j]= guard.direction
                
            else:
                print("Error, impossible condition")
                break
        # v
        if guard.direction == "v":
            i,j = guard.position
            if i == len(mapa)-1:
                mapa[i,j] ="X"
                # print("stepping out")
                break
            elif mapa[i+1,j] != "#":
                if globina == 0 and '#' not in test[i+1][j]:
                    copyGuard = guard.copy()
                    copyMapa = np.copy(mapa)
                    copyTest = copy.deepcopy(test)
                    copyMapa[i+1,j] = '#'
                    vsota+= krneki(copyGuard,copyMapa,copyTest,1)
                    test[i+1][j] += '#'
                if "v" in test[i+1][j]:
                    # print(str(i+1)+" "+str(j))
                    # print("CIKEL3")
                    # print(mapa)
                    return 1
                # print("cando")
                guard.position=(i+1,j)
                mapa[i,j] = "X"
                mapa[i+1,j] = guard.direction
                test[i][j] += guard.direction
                # test[i+1][j] += guard.direction
                # print(mapa[i,j])
            elif mapa[i+1,j] == "#":
                test[i][j] += guard.direction
                guard.turn()
                mapa[i,j]= guard.direction
            
            else:
                print("Error, impossible condition")
                break
        # <
        if guard.direction == "<":
            i,j = guard.position
            if j == 0:
                mapa[i,j] ="X"
                # print("stepping out")
                break
            elif mapa[i,j-1] != "#":
                if globina == 0 and '#' not in test[i][j-1]:
                    copyGuard = guard.copy()
                    copyMapa = np.copy(mapa)
                    copyTest = copy.deepcopy(test)
                    copyMapa[i,j-1] = '#'
                    vsota+= krneki(copyGuard,copyMapa,copyTest,1)
                    test[i][j-1] += '#'
                if "<" in test[i][j-1]:
                    # print(str(i)+" "+str(j-1))
                    # print("CIKEL4")
                    # print(mapa)
                    return 1

                guard.position=(i,j-1)
                mapa[i,j] = "X"
                test[i][j] += guard.direction
                mapa[i,j-1] = guard.direction
                
                # test[i][j-1] += guard.direction
                # print(mapa[i,j])
            elif mapa[i,j-1] == "#":
                test[i][j] += guard.direction
                guard.turn()
                mapa[i,j]= guard.direction
                
                
            else:
                print("Error, impossible condition")
                break
    # for vrsta in test:
    #     print(vrsta)
    return vsota

f = open("input.txt", "r")
mapa = []
i = 0
for line in f:
    line = line.strip()
    for j in range(len(line)):
        if line[j] != '.' and line[j] != '#':
            guard = Guard(line[j],(i,j))

    mapa.append(list(line))
    i+=1
test = mapa.copy()
mapa = np.array(mapa)
# print(test)
# print(mapa)
res = krneki(guard,mapa,test,0)
print(res)
# print(test[5,4])
    # elif guard.direction == ">":
        
    # elif guard.direction == "<":
    # elif guard.direction == "^":
