from DSU import DSU
from min_heap import MinHeap

class EdgeListGraph:
  class Vertex:
    def __init__(self,x):
      self.elem=x
    def element(self):
      return self.elem
    def __hash__(self):
      return hash(id(self))
    def __repr(self):
      return str(self.elem)
  class Edge:
    def __init__(self,u,v,x):
      self.origin=u
      self.destination=v
      self.elem=x
    def endpoints(self):
      return (self.origin,self.destination)
    def opposite(self,v):
      return self.destination if v is self.origin else self.origin
    def element(self):
      return self.elem
    def __hash__(self):
      return hash(id(self))

  def __init__(self,directed=False):
    self.directed=directed
    self.V=[]
    self.E=[]

  def is__directed(self):
    return self.directed
  def vertex_count(self):
    return len(self.V)
  def vertices(self):
    return self.V
  def edge_count(self):
    return len(self.E)
  def edges(self):
    return self.E

  def get_edge(self,u,v):    #O(m)
    for e in self.E:
      if self.origin is u and self.destination is v:
        return e
      if not self.directed and self.origin is v and self.destination is u:
        return e
    return None 
    
  def degree(self,v,outgoing=True):    #O(m)
    count=0
    for e in self.E:
      if self.directed:
        if (outgoing and self.origin is v) or (not outgoing and self.destination is v)
          count+=1
      elif (self.origin is v) or (self.destination is v):
        count+=1
    return count

  def incident_edges(self,v,outgoing=True):    #O(m)
    result=[]
    for e in self.E:
      if self.directed:
        if (outgoing and self.origin is v) or (not outgoing and self.destination is v):
          result.append(e)
      elif (self.origin is v) or (self.destination is v):
          result.append(e)
    return result

  def insert_vertex(self,x=None):    #O(1)
    v=self.Vertex(x)
    self.V.append(v)
    return v

  def insert_edge(self,u,v,x=None):    #O(1)
    if self.get_edge(u,v) is not None:
      raise ValueError("u and v are aldready adjecent")
    e=self.Edge(u,v,x)
    self.E.append(e)
    return e

  def remove_edge(self,e):      #time complexity: O(m)
    new_E=[]
    for edge in self.E:
      if edge is not e:
        new_E.append(edge)
    self.E=new_E

  def remove_vertex(self,v):    #time complexity: O(m+n)
    new_E=[]
    for edge in self.E:
      if (edge.origin is not v) and (edge.destination is not v):
        new_E.append(edge)
    self.E=new_E

    new_V=[]
    for vertex in self.V:
      if vertex is not v:
        new_V.append(vertex)
   self.V=new_V
  
  def dfs(self,u,discovered=None):
    if discovered is None:
      discovered={u:None}
    for e in self.incident_edges(u):  #O(m x n)
      v=e.opposite(u)
      if v not in discovered:
        discovered[v]=e
        self.dfs(v,discovered)
    return discovered

  def bfs(self,s):
    discovered={s:None}
    level=[s]                                              #The key difference                                                    
    while len(level)>0:                                    #DFS: A → B → D → backtrack → C.
      next_level=[]                                        #BFS: A → B → C → D.
      for u in level:
        for e in self.incident_edges(u):                  #O(mxn)
          v=e.opposite(u)
          if v not in discovered:
            discovered[v]=e
            next_level.append(v)
      level=next_level
    return discovered

  def kruskal(self):
    heap=MinHeap()
    for e in self.E:                    #mO(logm)
      heap.push(e.element(),e)
      dsu=DSU()
    for v in self.V:
      dsu.make_set(v)
    tree=[]
    while len(tree)<len(self.V)-1 and not heap.is_empty():
      weight,e=heap.pop_min()
      u,v=e.endpoints()
      if dsu.union(u,v):
        tree.append(e)
    return tree

  def boruvka(self):                # m Olog(n) #root->cheapest outgoing edge
    dsu=DSU()
    for v in self.V:
      dsu.make_set(v)
    tree=[]
    while True:
      cheapest={}
      for i in (len(self.E)):
        e=self.(E[i])
        ru=dsu.find(e.origin)
        rv=dsu.find(e.destination)
        if (ru==rv):
          continue
        for r in (ru,rv):
          if r not in cheapest or (e.element(),i)<cheapest[r][0]:
            cheapest=((e.element(),i),e)
      if(len(cheapest)==0):
        break
      for key,e in cheapest.values():
        if dsu.union(e.origin,e.destination):
          tree.append(e)
    return tree
            

  


        

      
  
