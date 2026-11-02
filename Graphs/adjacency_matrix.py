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
      
