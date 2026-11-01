class DSU:
    def __init__(self):
        self.parent={}
        self.rank={}
    def makset(self,x):
        self.parent[x]=x
        self.rank[x]=0
