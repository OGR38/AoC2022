import numpy as np

with open("input_d12") as f:
    l = np.array([list(map(lambda x: ord(x)-ord("a"),[*line.strip()])) for line in f.readlines()],int)

# with open("input_d12_test") as f:
#     l = np.array([list(map(lambda x: ord(x)-ord("a"),[*line.strip()])) for line in f.readlines()],int)
    
row_size = len(l)
column_size = len(l[0])

cost = np.zeros((row_size,column_size))
for i in range(row_size):
    for j in range(column_size):
        cost[i,j] = np.inf

def find_E():
    for i in range(row_size):
        for j in range(column_size):
            if l[i,j] == ord("E")-ord("a"):
                return([i,j])
def find_S():
    for i in range(row_size):
        for j in range(column_size):
            if l[i,j] == ord("S")-ord("a"):
                return([i,j])
            
[Ex,Ey] = find_E()
cost[Ex,Ey] = 0
[Sx,Sy] = find_S()

l[Ex,Ey] = ord("z")-ord("a")
l[Sx,Sy] = 0

def update_neighboors(pos):
    [x,y] = pos
    v = l[x,y]
    c = cost[x,y]
    if x-1 >= 0:
        if l[x-1,y] > v-2:
            if cost[x-1,y] > c+1:
                cost[x-1,y] = min(cost[x-1,y],c+1)
                update_neighboors([x-1,y])
    if x+1 < row_size:
        if l[x+1,y] > v-2:
            if cost[x+1,y] > c+1:
                cost[x+1,y] = min(cost[x+1,y],c+1)
                update_neighboors([x+1,y])
    if y-1 >= 0:
        if l[x,y-1] > v-2:
            if cost[x,y-1] > c+1:
                cost[x,y-1] = min(cost[x,y-1],c+1)
                update_neighboors([x,y-1])
    if y+1 < column_size:
        if l[x,y+1] > v-2:
            if cost[x,y+1] > c+1:
                cost[x,y+1] = min(cost[x,y+1],c+1)
                update_neighboors([x,y+1])

update_neighboors([Ex,Ey])
res = cost[Sx,Sy]
print(f"le coût minimal est de {res}")

# Part Two ..................................................

cost_from_a = [] 
for i in range(row_size):
    for j in range(column_size):
        if l[i,j] == 0:
            cost_from_a.append(cost[i,j])
            
res = min(cost_from_a)
print(f"Le coût minimal en partant d'un a est de {res}")

