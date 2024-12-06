import numpy as np
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
mapa = np.array(mapa)
# print(mapa)
# print(guard.position)
# print(guard)
# ^><v
while True:
    # ^
    if guard.direction == "^":
        i,j = guard.position
        if i == 0:
            mapa[i,j] ="X"
            print("stepping out")
            break
        elif mapa[i-1,j] != "#":
            guard.position=(i-1,j)
            mapa[i,j] = "X"
            mapa[i-1,j] = guard.direction
        elif mapa[i-1,j] == "#":
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
            print("stepping out")
            break
        elif mapa[i,j+1] != "#":
            # print("cando")
            guard.position=(i,j+1)
            mapa[i,j] = "X"
            mapa[i,j+1] = guard.direction
            # print(mapa[i,j])
        elif mapa[i,j+1] == "#":
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
            print("stepping out")
            break
        elif mapa[i+1,j] != "#":
            # print("cando")
            guard.position=(i+1,j)
            mapa[i,j] = "X"
            mapa[i+1,j] = guard.direction
            # print(mapa[i,j])
        elif mapa[i+1,j] == "#":
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
            print("stepping out")
            break
        elif mapa[i,j-1] != "#":
            # print("cando")
            guard.position=(i,j-1)
            mapa[i,j] = "X"
            mapa[i,j-1] = guard.direction
            # print(mapa[i,j])
        elif mapa[i,j-1] == "#":
            guard.turn()
            mapa[i,j]= guard.direction
            
        else:
            print("Error, impossible condition")
            break

    # break
print(mapa)
print(guard.direction)
print(np.sum(np.char.count(mapa,'X')))

