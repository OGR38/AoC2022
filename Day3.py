import numpy as np
from more_itertools import chunked
# import pandas as pd

# fonction list convertie une string en liste de caractère
# Use liste[:int(len(liste)/2-1)] liste[]

with open("input_d3") as f:
    ruck=[]
    l = f.readlines()
    while line := f.readline().strip():
        ruck.append(set(line))    
    ruckl = [ [ list(l[n].strip())[:int(len(list(l[n].strip()))/2)], list(l[n].strip())[int(len(list(l[n].strip()))/2):] ] for n in range(len(l))]

ruck_match = [set(depth[0]) & set(depth[1]) for depth in ruckl]
   
def value_letter(s):
    for lettre in s:
        if ord(lettre) < 91:
            return(ord(lettre)- 65+27)
        else:
            return(ord(lettre)-97+1)
        
print(sum(map(value_letter,ruck_match)))

# badge = []

# for n in range(int(len(l)/3)):
#     badge.append(ruck[3*n] & ruck[3*n+1] & ruck[3*n+2])

# print(sum(map(value_letter,badge)))
