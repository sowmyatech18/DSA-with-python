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

  
