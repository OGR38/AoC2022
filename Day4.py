import numpy as np
from more_itertools import chunked

with open("input_d4") as f:
    l = f.readlines()
    pairs=[list(map(int,n.strip().replace(',','-').split('-'))) for n in l]
    
counter=0
for elem in pairs:
    if elem[0]==elem[2] and elem[3]==elem[1]:
        counter+=1
    elif elem[0]<=elem[2] and elem[3]<elem[1]:
        counter +=1
    elif elem[0]<elem[2] and elem[3]<=elem[1]:
        counter +=1
    elif elem[2]<=elem[0] and elem[1]<elem[3]:
        counter +=1
    elif elem[2]<elem[0] and elem[1]<=elem[3]: 
        counter +=1
print(counter)

counter=0
for elem in pairs:
    if elem[0]<=elem[2] and elem[3]<=elem[1]:
        counter +=1
    elif elem[0]<=elem[2] and elem[2]<=elem[1] and elem[1]<elem[3]:
        counter +=1
    elif elem[2]<elem[0] and elem[0]<=elem[3]:
        counter +=1
print(counter)


#pairs_test=[[2,4,6,8],[2,3,4,5],[7,9,7,9],[2,8,3,7],[6,6,4,6],[2,6,4,8]]

