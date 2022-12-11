from more_itertools import chunked

with open("input_d11") as f:
    l = list(chunked(f.readlines(),7))

# with open("input_d11_test") as f:
#     l = list(chunked(f.readlines(),7))

class monkey:
    def __init__(self):
        self.name = -1
        self.operation = (lambda x: x)
        self.item = []
        self.divider = 1
        self.action = {True: -1, False: -1}

#Part One..........................................................
all_monkeys =[]

for line in l:
    m = monkey()
    
    m.name = int(line[0].strip().replace(":"," ").split()[-1])

    for elem in line[1].replace(","," ").strip().split()[2:]:
        m.item.append(int(elem))

    stri=" ".join(e for e in list(line[2].strip().split()[3:]))
    def ope(old,stri=stri):
        return(eval(stri))
    m.operation = ope 

    m.divider = int(line[3].strip().split()[-1])

    m.action = {True: int(line[4].strip().split()[-1]), False: int(line[5].strip().split()[-1])}

    all_monkeys.append(m)

inspection = [0,0,0,0,0,0,0,0,0]    

for n in range(20):
    for m in all_monkeys:
        inspection[m.name] += len(m.item)
        for elem in m.item:
            new = m.operation(elem) // 3
            all_monkeys[m.action[(new % m.divider) == 0]].item.append(new)
        m.item=[]

best=sorted(inspection)
monkey_buisness=best[-1]*best[-2]
print(f"Le Monkey Buisness est de {monkey_buisness}")

#Part Two..........................................................
all_monkeys =[]

for line in l:
    m = monkey()
    
    m.name = int(line[0].strip().replace(":"," ").split()[-1])

    for elem in line[1].replace(","," ").strip().split()[2:]:
        m.item.append(int(elem))

    stri=" ".join(e for e in list(line[2].strip().split()[3:]))
    def ope(old,stri=stri):
        return(eval(stri))
    m.operation = ope 

    m.divider = int(line[3].strip().split()[-1])

    m.action = {True: int(line[4].strip().split()[-1]), False: int(line[5].strip().split()[-1])}

    all_monkeys.append(m)

inspection = [0,0,0,0,0,0,0,0,0]  

modulo = 1
for m in all_monkeys:
    modulo = modulo*m.divider

for n in range(10000):
    for m in all_monkeys:
        inspection[m.name] += len(m.item)
        for elem in m.item:
            new = m.operation(elem) % modulo
            all_monkeys[m.action[(new % m.divider) == 0]].item.append(new)
        m.item=[]        

best=sorted(inspection)
monkey_buisness=best[-1]*best[-2]
print(f"Le Monkey Buisness v2 est de {monkey_buisness}")
