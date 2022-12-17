import numpy as np
from more_itertools import chunked

with open("input_d14") as f:
    l = [list(map(list,map(reversed,chunked(list(map(int,line.replace("->"," ").replace(","," ").strip().split())),2)))) for line in f.readlines()]

# with open("input_d14_test") as f:
#     l = [list(map(list,map(reversed,chunked(list(map(int,line.replace("->"," ").replace(","," ").strip().split())),2)))) for line in f.readlines()]    

Row_min=min(elem[0] for line in l for elem in line)
Row_max=max(elem[0] for line in l for elem in line)    
Col_min=min(elem[1] for line in l for elem in line)
Col_max=max(elem[1] for line in l for elem in line)

print(f"Les lignes vont de {Row_min} à {Row_max} et les colonnes vont de {Col_min} à {Col_max}")
## Part One .....................................................
# scene=np.chararray((Row_max+10,Col_max+10),unicode=True)
# scene[:] = "."

# for line in l:
#     for n in range(len(line)-1):
#         [x1,y1]=line[n]
#         [x2,y2]=line[n+1]
#         if x1==x2:
#             for y in range(min(y1,y2),max(y1,y2)+1):
#                 scene[x1,y] = "#"
#         if y1==y2:
#             for x in range(min(x1,x2),max(x1,x2)+1):
#                 scene[x,y1] = "#"

def plot_scene():
    for line in scene:
        ligne=""
        for elem in list(line)[Col_min-1:Col_max+1]:
            ligne+=elem
        print(ligne)
        
# plot_scene()                
# counter=0
# infini=False
# while not infini:
#     [x,y]=[0,500]
#     c = [scene[x+1,y-1],scene[x+1,y],scene[x+1,y+1]]
#     while (x!= Row_max+1) and (c[0] == "." or c[1] == "." or c[2] =="."):
#         if c[1] == ".":
#             x += 1
#         elif c[1] != "." and c[0] == ".":
#             x+=1
#             y+=-1
#         elif c[0] != "." and c[1] != "." and c[2] == ".":
#             x+=1
#             y+=1
#         c = [scene[x+1,y-1],scene[x+1,y],scene[x+1,y+1]]
#         print([x,y])
#         print(c)
#     if x != Row_max+1:
#         scene[x,y] = "o"
#         counter+=1
#     else:
#         infini=True
#     #plot_scene()

# print(f"Le nombre de grains avant l'infini est de {counter}")

# Part Two ...................................................................
scene=np.chararray((Row_max+10,Col_max+2*Row_max),unicode=True)
scene[:] = "."
scene[Row_max+2:] = "#"

for line in l:
    for n in range(len(line)-1):
        [x1,y1]=line[n]
        [x2,y2]=line[n+1]
        if x1==x2:
            for y in range(min(y1,y2),max(y1,y2)+1):
                scene[x1,y] = "#"
        if y1==y2:
            for x in range(min(x1,x2),max(x1,x2)+1):
                scene[x,y1] = "#"


counter=0
stucked=False
while not stucked:
    [x,y]=[0,500]
    c = [scene[x+1,y-1],scene[x+1,y],scene[x+1,y+1]]
    while (c[0] == "." or c[1] == "." or c[2] =="."):
        if c[1] == ".":
            x += 1
        elif c[1] != "." and c[0] == ".":
            x+=1
            y+=-1
        elif c[0] != "." and c[1] != "." and c[2] == ".":
            x+=1
            y+=1
        c = [scene[x+1,y-1],scene[x+1,y],scene[x+1,y+1]]
        #print([x,y])
        #print(c)
    if x != 0:
        scene[x,y] = "o"
        counter+=1
    else:
        counter+=1
        stucked=True
    #plot_scene()

print(f"Le nombre de grains avant d'être kéblo est de {counter}")
