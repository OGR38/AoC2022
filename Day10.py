with open("input_d10") as f:
    l = [line.split() for line in f.readlines()]

#with open("input_d10_test") as f:
#    l = [line.split() for line in f.readlines()]
    
#Building a list s.t. cycle[n] is the value of X after the n cycle, or alternatively, the value of X during the n+1 cycle    
cycle=[1]

for line in l:
    if line[0] == "noop":
        cycle.append(cycle[-1])
        #print(cycle[-1])
    elif line[0] == "addx":
        #print(line[0]+line[1])
        cycle.append(cycle[-1])
        cycle.append(cycle[-1]+int(line[1]))
        #print(cycle[-2])
        #print(cycle[-1])
res = sum([(20+40*n)*cycle[20+40*n-1] for n in range(6)])
print(res)

for n in range(6):
    row=""
    for m in range(40):
        sprite=cycle[40*n+m]
        if m==sprite-1 or m==sprite or m==sprite+1:  
            row=row+"#"
        else:
            row=row+"."
    print(row)
    
