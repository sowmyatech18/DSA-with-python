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
    
  def remove_edge(self,e):   #O(deg(u) +deg(v) +m)
    u,v=e.endpoints()

    new_out=[]
    for edge in self.outgoing[u]:
      if edge is not e:
        new_out.append(edge)
    self.outgoing[u]=new_out
    new_in=[]
    for edge in self.incoming[v]:
      if edge is not e:
        new_in.append(edge)
    self.incoming[v]=e
    new_E=[]
    for edge in self.E:
      if edge is not e:
        new_E.append(edge)
    self.E=new_E

  def remove_vertex(self,v):    #O(m+n)
    new_E=[]
    for e in self.E:
      if e.origin is not v and e.destination is not v:
        new_E.append(e)
    self.E=new_E

    new_out={}
    for vertex in self.outgoing:
      if vertex is not v:
        new_out[vertex]=[]
        for e in self.outgoing[vertex]:
          if e.origin is not v and e.destination is not v:
            new_out[vertex].append(e)
    self.outgoing=new_out

    if self.directed:
      new_in={}
      for vertex in self.incoming:
        if vertex is not v:
          new_in[vertex]=[]
          for e in self.incoming[vertex]:
            if e.origin is not v and e.destination is not v:
              new_in[vertex].append(e)
      self.incoming=new_in

  def dfs(self,u,discovered=None):    #O(n+m)
    if discovered is None:
      discovered={u:None}
    for e in self.incident_edges(u):
      v=e.opposite(u)
      if v not in discovered:
        discovered[v]=e
        self.dfs(v,discovered)
    return discovered

  def bfs(self,s):        #O(n+m)
    discovered={s:None}
    level=[s]
    while len(level)>0:
      next_level=[]
      for e in self.incident_edges(s):
        v=e.opposite(s)
        if v not in discovered:
          discovered[v]=e
          next_level.append(v)
      level=next_level
    return discovered

def prim_mst(self,s):
  d={}
  connect={}
  pq=PriorityQueue()
  loactors={}
  for v in self.vertcices():
    d[v]=0 if v is s else float('inf')
      locatosr=pq.add(d[v],v)
  tree=[]
  while is not pq.is_empty():
    key,u=pq.remove_min()
    new_loc={}
    for vertex in locators:
      if vertex is not u:
        new_loc[vertex]=locators[vertex]
    locator=new_loc
    if u in connect:
      tree.append(connect[u])
    for e in self.incident_edges(u):
      v=e.opposite(u)
      if v in locators and e.element()<d[v]:
        d[v]=e.element()
        connect[v]=e
        pq.update(locators[v],d[v],v)
  return tree

def dijkstra(self,s):
    dist={}
    parent={s:None}
    pq=PriorityQueue()
    locators={}
    for v in self.vertices:
      dist[v]=0 if v is s else float('inf')
        locators=pq.add(dist[v],v)
    while is not pq.is_empty():
      key,u=pq.remove_min()
      new_loc={}
      for vertex in locators:
        if vertex is not u:
          new_loc[vertex]=locators[vertex]
      locators=new_loc
      for e in self.incident_edges(u):
        v=opposite(u)
        if v in locators and dist[u]+ e.element()<dist[v]:
          dist[v]=dist[u]+e.element()
          parent[v]=e
          pq.update(locators[v],dict[v],v)
    return dist,parent
  
          
    
    
    
    
  
        
    

  
    

    
      
