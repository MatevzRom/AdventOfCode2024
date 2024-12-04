import numpy as np
f = open("input.txt", "r")
arr = []
for line in f:
    line = line.strip()
    arr.append(list(line))

# print(arr)
arr = np.array(arr)
# print(arr[0])
# print(arr[0][1])
sum=0
r = 0
l = 0
u = 0
d= 0
cmaj = 0
cmin = 0
desno = np.array(["X","M","A","S"]) #could use for down as well
levo = np.array(["S","A","M","X"])
krneki = np.copy(arr)
krneki = np.rot90(arr)
# print(krneki)

for i in range(len(arr)):
    for j in range(len(arr[0])):
        temp1 = arr[i,j:j+4]
        # Right
        if temp1.shape == desno.shape and np.all(temp1 == desno):
            sum+=1
            r+=1   
        # Left
        if temp1.shape == levo.shape and np.all(temp1 == levo):
            sum+=1
            l+=1
        temp2 = arr[i:i+4,j]
        # Down
        if temp2.shape == desno.shape and np.all(temp2 == desno):
            sum+=1
            d+=1
        # Up
        if temp2.shape == levo.shape and np.all(temp2 == levo):
            sum+=1
            u+=1
        # Crisscross
        
        temp3 = np.diagonal(arr,j-i)
        # Major diag:
        # print(str(i)+" "+str(j))
        # print(temp3)
        mansi = min(i,j)
        if temp3[mansi:mansi+4].shape == desno.shape and (np.all(temp3[mansi:mansi+4] == desno) or np.all(temp3[mansi:mansi+4] == levo)):
            # print("found")
            sum+=1
            cmaj+=1
        # Minor diag:
        temp4 = np.diagonal(krneki,j-i)
        
        if temp4[mansi:mansi+4].shape == desno.shape and (np.all(temp4[mansi:mansi+4] == desno) or np.all(temp4[mansi:mansi+4] == levo)):
            sum+=1
            cmin+=1
print(sum)
# print("[r,l,u,d,cmaj,cmin]")
# print([r,l,u,d,cmaj,cmin])

        