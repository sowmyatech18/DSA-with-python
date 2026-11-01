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
      if (self.origin is not v) and (self.destination is not v):
        new_E.append(edge)
    self.E=new_E

    new_V=[]
    for vertex in self.V:
      if vertex is not v:
        new_V.append(v)
   self.V=new_V

      
  
