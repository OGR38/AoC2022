import numpy as np
from more_itertools import chunked
import csv

#             [G] [W]         [Q]    
# [Z]         [Q] [M]     [J] [F]    
# [V]         [V] [S] [F] [N] [R]    
# [T]         [F] [C] [H] [F] [W] [P]
# [B] [L]     [L] [J] [C] [V] [D] [V]
# [J] [V] [F] [N] [T] [T] [C] [Z] [W]
# [G] [R] [Q] [H] [Q] [W] [Z] [G] [B]
# [R] [J] [S] [Z] [R] [S] [D] [L] [J]
#  1   2   3   4   5   6   7   8   9 

# cra = np.loadtxt("input_d5")[:, 1] Problem string to float

with open("input_d5") as f:
    l = reversed(list(f.readlines()))
    cra = [[],[],[],[],[],[],[],[],[]]
    for line in l:
        lineb = list(line.replace('\n',' '))
        for n in range((len(lineb) // 4)):
            lettre=lineb[4*n+1]
            if lettre!=" ":
                cra[n].append(lettre)

with open("input_d5_bis") as f:
    ins = f.readlines()

crap1=cra
for line in ins:
    lb=line.split()
    num=int(lb[1])
    dep=int(lb[3])-1
    arr=int(lb[5])-1
    for n in reversed(crap1[dep][-num:]):
        crap1[arr].append(n)
    crap1[dep]=crap1[dep][:-num]

for line in crap1:
    print(line[-1])

print("\n")

crap2=cra
for line in ins:
    lb=line.split()
    num=int(lb[1])
    dep=int(lb[3])-1
    arr=int(lb[5])-1
    for n in crap2[dep][-num:]:
        crap2[arr].append(n)
    crap2[dep]=crap2[dep][:-num]

for line in crap2:
    print(line[-1])
