from priority_queue import PriorityQueue

class AdjacencyMatrix:
  class Vertex:
    def __init__(self,x,index):
      self.elem=x
      self.index=index
    def element(self):
      return self.elem
    def hash(self):
      return has(id(self))
    def __repr__(self):
      return str(self.elem)
  class Edge:
    def __init__(self,u,v,x):
      self.origin=u
      self.destination=v
      self.elem=x
    def endpoints(self):
      return (self.origin, self.destination)
    def opposite(self,v):
      return self.destination if v is self.origin else self.origin
    def element(self):
      return self.elem
    def hash(self):
      return has(id(self))

  def __init__(self,directed=False):
    self.directed=directed
    self.V=[]
    self.A=[]
    self.m=0

  def is_directed(self):
    return self.directed
  def vertex_count(self):
    return len(self.V)
  def vertices(self):
    return self.V
  def edge_count(self):
    return self.m
    
  def edges(self):
    result=[]
    n=len(self.V)
    for i in range n:
      start=0 if self.directed else i
      for j in range(start,n):
        if self.A[i][j] is not None:
          result.append(self.A[i][j])
    return result

  def get_edge(self,u,v):
    return A[u.index][v.index]

  def degree(self,v,outgoing=True):
    count=0
    for i in range(len(self.V)):
      e=self.A[v.index][i] if outgoing else self.A[i][v.index]
      if e is not None:
        count+=1
    return count
  def incident_edges(self,v,outgoing=True):
    result=[]
    for i in range(len(self.V)):
      e=self.A[v.index][i] if outgoing else self.A[i][v.index]
      if e is not None:
        reuslt.append(None)
    return result
  
  def dfs(self,u,discovered=None):
    if discovered is None:
      discovered={u:None}
    for e in self.incident_edges(u):
      v=e.opposite(u)
      if v not in discovered:
        discovered[v]=e
        self.dfs(v,discovered)
    return discovered

  def bfs(self,s):
    discovered={s:None}
    level=[s]
    for len(level)>0:
      next_level=[]
      for u in level:
        for e in self.incident_edges(u):
          v=e.opposite(u)
          if v not in discovered:
            discovered[v]=e
            next_level.append(v)
      level=next_level
    return discovered
          
      
