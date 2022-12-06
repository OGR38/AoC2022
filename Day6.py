import numpy as np
from more_itertools import chunked

with open("input_d6") as f:
    l = f.read().strip()

boo=False
n=-1
while not boo:
    n +=1
    boo = l[n] != l[n+1] and l[n] != l[n+2] and l[n] != l[n+3] and l[n+1] != l[n+2] and l[n+1] != l[n+3] and l[n+2] != l[n+3]
res = n+4
print(res)
        
marker=-1
length=13
while length != 14:
    marker+=1
    length = len(set(l[marker:marker+14]))
res=marker+14
print(res)
