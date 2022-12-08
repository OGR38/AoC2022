import numpy as np
from more_itertools import chunked

with open("input_d8") as f:
    l = [line.split() for line in f.readlines()]
    lb = [list(map(int,list(line[0]))) for line in l]
    forest = np.array(lb,int)


#forest = np.array([[3,0,3,7,3],[2,5,5,1,2],[6,5,3,3,2],[3,3,5,4,9],[3,5,3,9,0]],int)    
size=len(forest) 
#print(size)

counter = 2*size + 2*(size-2)
#print(counter)
for i in range(size-2):
    for j in range(size-2):
        m1 = max(forest[i+1,:j+1])
        m2 = max(forest[:i+1,j+1])
        m3 = max(forest[i+1,j+2:])
        m4 = max(forest[i+2:,j+1])
        m = min(m1,m2,m3,m4)
        #print(m)
        if forest[i+1,j+1] > m:
            counter += 1
print(counter)

scenic_score=0
for i in range(size-2):
    for j in range(size-2):
        m = forest[i+1,j+1]
        n1 = 1
        n2 = 1
        n3 = 1
        n4 = 1
        while i+1-n1 != 0 and forest[i+1-n1,j+1] < m:
            n1 += 1
        while j+1-n2 != 0 and forest[i+1,j+1-n2] < m:
            n2 += 1
        while i+1+n3 != size-1 and forest[i+1+n3,j+1] < m:
            n3 += 1
        while j+1+n4 != size-1 and forest[i+1,j+1+n4] < m:
            n4 += 1
        #print(n1,n2,n3,n4)
        scenic_score = max(scenic_score,n1*n2*n3*n4)
print(scenic_score)
