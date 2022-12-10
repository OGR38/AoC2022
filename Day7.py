with open("input_d7") as f:
    l=f.readlines()
    term=[elem.strip().split() for elem in l]

# with open("input_d7_test") as f:
#     l=f.readlines()
#     term=[elem.strip().split() for elem in l]

class dire:
    def __init__(self,dir_name,posinit):
        self.name = dir_name
        self.size = 0
        self.children = []
        self.posdeb = posinit
        self.length = 0
    def append(self,d):
        self.size+=d.size
        self.children.append(d)
    def find(self,subdir_name):
        for elem in self.children:
            if elem.name == subdir_name:
                return(elem)
    def build_tree(self):
        comm = term[self.posdeb:]
        m=0
        while m < len(comm):
            line = comm[m]
            if line[0] == "$":
                if line[1] == "cd":
                    nom=line[2]
                    if nom == "..":
                        self.length = m
                        break
                    else:
                        suite=self.find(nom)
                        suite.posdeb = self.posdeb+m+1
                        suite.build_tree()
                        m += suite.length +2
                else:
                    m +=1
            else:
                if line[0] == "dir":
                    self.append(dire(line[1],0))
                else:
                    self.size += int(line[0])
                m += 1
    def update_size(self):
        for elem in self.children:
            elem.update_size()
            self.size += elem.size
    def sum_size_most(self):
        total_size=0
        if self.size <= 100000:
            total_size+=self.size
        for elem in self.children:
            total_size += elem.sum_size_most()
        return(total_size)
    def max_less_than(self,limit):
        counter=70000000
        if self.size >= limit:
            counter=min(counter,self.size)
        for elem in self.children:
            counter=min(counter,elem.max_less_than(limit))
        return(counter)
home=dire("/",1)
home.build_tree()
home.update_size()

print(f"Le total recherche est de {home.sum_size_most()}")

size_to_free = 30000000 - (70000000-home.size)

print(f"La taille minimal a liberer est {home.max_less_than(size_to_free)}")
