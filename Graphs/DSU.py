class DSU:
    def __init__(self):
        self.parent={}
        self.rank={}
    def makset(self,x):
        self.parent[x]=x
        self.rank[x]=0
    def find(self,x):
        if(self.parent[x]!=x):
            self.parent[x]=find(self.parent[x])  #path compression
        return self.parent[x]
    def union(self,x,y):
        rx=self.find(x)
        ry=self.find(y)
        if(rx==ry):
            return False
        if(self.rank[rx]<self.rank[ry]):  #union by rank
            self.parent[rx]=ry
        elif(self.rank[rx]>self.rank[ry]):
            self.parent[ry]=rx
        else:
            self.parent[ry]=rx
            self.rank[rx]+=1
        return True
dsu=DSU()
dsu.make_set(0)
dsu.make_set(1)
dsu.make_set(2)
dsu.make_set(3)

dsu.union(0, 1)
dsu.union(2, 3)
dsu.union(0, 2)

print(dsu.parent)
print(dsu.rank)
