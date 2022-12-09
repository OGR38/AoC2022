import numpy as np
from more_itertools import chunked

with open("input_d9") as f:
    l = [line.split() for line in f.readlines()]
    
#l = [["R", "4"],["U","4"],["L","3"],["D","1"],["R","4"],["D","1"],["L","5"],["R","2"]]

# We start by computing the size of the maximal grid    
num_L = 0
num_R = 0
num_U = 0
num_D = 0
for line in l:
    le=line[0]
    nu=int(line[1])
    if le == "L":
        num_L += nu
    elif le == "R":
        num_R += nu
    elif le == "U":
        num_U += nu
    elif le == "D":
        num_D += nu
print(num_L,num_R,num_U,num_D)

grid=np.zeros((num_U+num_D+1,num_L+num_R+1),int)
grid[num_U,num_L]=1
H=[num_U,num_L]
T=[num_U,num_L]

for line in l:
    n = int(line[1])
    direction = line[0]
    for k in range(n):
        if direction == "U":
            H[0] += -1
        elif direction == "D":
            H[0] += +1
        elif direction == "L":
            H[1] += -1
        elif direction == "R":
            H[1] += +1
        if abs(H[0]-T[0]) // 2 == 1:
            T[0] += (H[0]-T[0]) // 2
            T[1] += (H[1]-T[1])
        elif abs(H[1]-T[1]) // 2 == 1:
            T[0] += (H[0]-T[0])
            T[1] += (H[1]-T[1]) // 2
        
        grid[T[0],T[1]] = 1
print(np.sum(grid))

grid=np.zeros((num_U+num_D+1,num_L+num_R+1),int)
grid[num_U,num_L]=1
M=[[num_U,num_L],[num_U,num_L],[num_U,num_L],[num_U,num_L],[num_U,num_L],[num_U,num_L],[num_U,num_L],[num_U,num_L],[num_U,num_L],[num_U,num_L]]

def move(H,T):
    if abs(H[0]-T[0]) // 2 == 1 and abs(H[1]-T[1]) // 2 == 1:
        T[0] += (H[0]-T[0]) // 2
        T[1] += (H[1]-T[1]) // 2
    elif abs(H[0]-T[0]) // 2 == 1 and abs(H[1]-T[1]) // 2 == 0:
        T[0] += (H[0]-T[0]) // 2
        T[1] += (H[1]-T[1])
    elif abs(H[0]-T[0]) // 2 == 0 and abs(H[1]-T[1]) // 2 == 1:
        T[0] += (H[0]-T[0])
        T[1] += (H[1]-T[1]) // 2

for line in l:
    n = int(line[1])
    direction = line[0]
    for k in range(n):
        if direction == "U":
            M[0][0] += -1
        elif direction == "D":
            M[0][0] += +1
        elif direction == "L":
            M[0][1] += -1
        elif direction == "R":
            M[0][1] += +1
        for n in range(len(M)-1):
            move(M[n],M[n+1])
        grid[M[-1][0],M[-1][1]] = 1
print(np.sum(grid))
