import numpy as np

with open("input_d2") as f:
    l = f.read()
    li1 = [l[4*n] for n in range(int(len(l)/4))]
    li2 = [l[4*n+2] for n in range(int(len(l)/4))]

def score(l1,l2):
    score=0
    l1nombre=[]
    l2nombre=[]
    for lettre in l1:
        if lettre == "A":
            l1nombre.append(1)
        elif lettre == "B":
            l1nombre.append(2)
        elif lettre == "C":
            l1nombre.append(3)
        else:
            print("error")
    for lettre in l2:
        if lettre == "X":
            l2nombre.append(1)
        elif lettre == "Y":
            l2nombre.append(2)
        elif lettre == "Z":
            l2nombre.append(3)
        else:
            print("error")
    for n in range(len(l1nombre)):
        score += l2nombre[n]
        if l1nombre[n]==l2nombre[n]:
            score += 3
        elif l2nombre[n] - l1nombre[n] %3 == 1:
            score += 6
    print(f"Mon score total est de {score}")

score(li1,li2)

#X lose ie 2 mod 3 Y draw ie 0 mod 3 Z win ie 1 mod 3

def goodgame(l1,res):
    l1nombre=[]
    resnombre=[]
    goodcombo=[]
    score=0
    for lettre in l1:
        if lettre == "A":
            l1nombre.append(1)
        elif lettre == "B":
            l1nombre.append(2)
        elif lettre == "C":
            l1nombre.append(3)
        else:
            print("error")
    for lettre in res:
        if lettre == "X":
            resnombre.append(-1)
        elif lettre == "Y":
            resnombre.append(0)
        elif lettre == "Z":
            resnombre.append(1)
        else:
            print("error")
    for n in range(len(l1nombre)):
        score += (resnombre[n]+1)*3 + ((l1nombre[n]-1+resnombre[n]) %3) + 1
    print(f"Mon score total est de {score}")

goodgame(li1,li2)

# score(li1,goodgame(li1,li2))
