from priority_queue import PriorityQueue

class AdjacencyList:
  class Vertex:
    def __init__(self,x):
      self.elem=x
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
      return (self.origin,self.destination)
    def opposite(self,v):
      return self.destination if v is self.origin else self.origin
    def element(self):
      return self.elem
    def hash(self):
      return hash(id(self))
  def __init__(self,directed=False):
    self.directed=directed
    self.outgoing={}
    self.incoming={} if self.directed else self.outgoing
    self.E=[]

  def is_directed(self):
    return self.directed
  def vertex_count(self):
    return len(self.outgoing)
  def vetrices(self):
    return list(self.outgoing.keys())
  def edge_count(self):
    return len(self.E)
  def edges(self):
    return self.E
  def get_edges(self,u,v):              #O(deg(u))
    for e in self.outgoing[u]:
      if e.oppsoite(v) is u:
        return e
    return None
  def degree(self,v,outgoing=True):      #O(1)
    if outgoing:
      return len(self.outgoing[v])
    return len(self.incoming[v])
  def incident_edges(self,v,outgoing=True):    #O(deg(v))
    if outgoing:
      return self.outgoing[v]
    return self.incoming[v]
  def insert_vertex(self,x=None):      #O(1)
    v=self.Vertex(x)
    self.outgoing[v]=[]
    if self.directed:
      self.incoming[v]=[]
    return v
  def insert_edge(self,u,v,x=None):    #O(1)
    if self.get_edge(u,v) is not None:
      raise ValueError("u and v are aldready adjacent")
    e=self.Edge(u,v,x)
    self.E.append(e)
    self.outgoing[u].append(e)
    self.incoming[v].append(e)
    return e 

  
    

    
      
