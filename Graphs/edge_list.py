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
