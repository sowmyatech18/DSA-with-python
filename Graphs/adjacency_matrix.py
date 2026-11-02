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
          
      
