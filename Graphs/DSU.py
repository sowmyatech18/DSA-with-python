class DSU:
    def __init__(self):
        self.parent={}
        self.rank={}
    def makset(self,x):
        self.parent[x]=x
        self.rank[x]=0
    def find(self,x):
        if(self.parent[x]!=x):
            self.parent[x]=find(self.parent[x])
        return self.parent[x]
