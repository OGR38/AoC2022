import numpy as np
import pandas as pd

lec=list(open("input_d1"))
# print(lec[0]+lec[1])
# print(int(lec[0])+int(lec[1]))

print(lec[2])

print(type(lec[2]))


def max_cal_cumul(liste):
    global_counter=0
    current_counter=0
    for depth in liste:
        if depth == "\n":
            global_counter=max(global_counter,current_counter)
            current_counter=0
        else:
            current_counter=current_counter+int(depth)
    global_counter=max(global_counter,current_counter)
    print("Le maximum des calories cumulées portée par un elfe est {}".format(global_counter))

liste_test_1=["12","\n","100","200","\n","1000"]
liste_test_2=["12","\n","100","200","\n","2"]

max_cal_cumul(liste_test_1)
max_cal_cumul(liste_test_2)


max_cal_cumul(lec)


def make_liste_cumul(liste):
    cumul_lec=[]
    current_counter=0
    for depth in liste:
        if depth=="\n":
            cumul_lec.append(current_counter)
            current_counter=0
        else:
            current_counter=current_counter+int(depth)
    cumul_lec.append(current_counter)
    return(cumul_lec)

lett1=make_liste_cumul(liste_test_1)
lecbis=make_liste_cumul(lec)

print(max(lecbis))

def findmaxkill(liste):
    maxloc=0
    place=-1
    killedliste=liste
    firstmax=0
    secondmax=0
    thirdmax=0
    for n in range(len(killedliste)):
        if liste[n]>maxloc:
            maxloc=liste[n]
            place=n
    firstmax=maxloc
    maxloc=0
    killedliste[place]=0
    for n in range(len(killedliste)):
        if liste[n]>maxloc:
            maxloc=liste[n]
            place=n
    secondmax=maxloc
    maxloc=0
    killedliste[place]=0
    for n in range(len(killedliste)):
        if liste[n]>maxloc:
            maxloc=liste[n]
            place=n
    thirdmax=maxloc
    madmax=firstmax+secondmax+thirdmax
    print("Le max porté par la somme des trois elfes est {}".format(madmax))

findmaxkill(lecbis)

#count_increase(make_sliding_window_liste(liste_elves_calories))

# def count_increase(liste):
#     counter=0
#     length_liste=len(liste)
#     for n in range(length_liste-1):
#      if int(liste[n]) < int(liste[n+1]):
#          counter=counter+1
         
#     print("La liste a une longueur de {} \n La liste a {} incréments \n".format(len(liste),counter))
            
# # def count_increase_2(liste):
# #     counter=0
# #     old_depth=1e10
# #     l=[]
# #     for depth in liste:
# #         if int(depth) > old_depth:
# #             l.append(int(depth))
# #             counter+=1
# #         old_depth=int(depth)
         
# #     print("La liste a une longueur de " + str(len(liste)))
# #     print("La liste a {} incréments \n".format(counter))

# #     return l
   
# def make_sliding_window_liste(liste):
#     newliste=[]
#     for n in range(len(liste)-2):
#         newliste.append(int(liste[n])+int(liste[n+1])+int(liste[n+2]))
#     return newliste

# liste_test=[0,-2,10,5,20]
# # count_increase_2(liste_test)

# liste_test_2=[199,200,208,210,200,207,240,269,260,263]
# # count_increase_2(liste_test_2)
# nl=make_sliding_window_liste(liste_test_2)
# count_increase(nl)




