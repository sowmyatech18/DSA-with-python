# Adjacency List graph: each vertex keeps a list of its incident edges
# (best: sparse graph, neighbour-driven algorithms -> DFS, BFS, Prim, Dijkstra)
from priority_queue import PriorityQueue


class AdjacencyListGraph:
    class Vertex:
        def __init__(self, x):
            self.elem = x

        def element(self):
            return self.elem

        def __hash__(self):
            return hash(id(self))

        def __repr__(self):
            return str(self.elem)

    class Edge:
        def __init__(self, u, v, x):
            self.origin = u
            self.destination = v
            self.elem = x

        def endpoints(self):
            return (self.origin, self.destination)

        def opposite(self, v):
            return self.destination if v is self.origin else self.origin

        def element(self):
            return self.elem

        def __hash__(self):
            return hash(id(self))

    def __init__(self, directed=False):
        self.directed = directed
        self.outgoing = {}                                 # vertex -> [edges out]
        self.incoming = {} if directed else self.outgoing  # undirected: same dict
        self.E = []

    def is_directed(self):
        return self.directed

    def vertex_count(self):
        return len(self.outgoing)

    def vertices(self):
        return list(self.outgoing.keys())

    def edge_count(self):
        return len(self.E)

    def edges(self):
        return self.E

    def get_edge(self, u, v):                              # O(deg(u))
        for e in self.outgoing[u]:
            if e.opposite(u) is v:
                return e
        return None

    def degree(self, v, outgoing=True):                    # O(1)
        if outgoing:
            return len(self.outgoing[v])
        return len(self.incoming[v])

    def incident_edges(self, v, outgoing=True):            # O(deg(v))
        if outgoing:
            return self.outgoing[v]
        return self.incoming[v]

    def insert_vertex(self, x=None):                       # O(1)
        v = self.Vertex(x)
        self.outgoing[v] = []
        if self.directed:
            self.incoming[v] = []
        return v

    def insert_edge(self, u, v, x=None):                   # O(1) (+ O(deg) check)
        if self.get_edge(u, v) is not None:
            raise ValueError('u and v are already adjacent')
        e = self.Edge(u, v, x)
        self.E.append(e)
        self.outgoing[u].append(e)
        self.incoming[v].append(e)
        return e

    def remove_edge(self, e):       #\(O(\deg(u)+\deg(v)+m)\)
        u, v = e.endpoints()

        new_out = []
        for edge in self.outgoing[u]:
            if edge is not e:
                new_out.append(edge)
        self.outgoing[u] = new_out

        new_in = []
        for edge in self.incoming[v]:
            if edge is not e:
                new_in.append(edge)
        self.incoming[v] = new_in

        new_E = []
        for edge in self.E:
            if edge is not e:
                new_E.append(edge)
        self.E = new_E

    def remove_vertex(self, v):         #- \(O(n+m)\)
        new_E = []
        for e in self.E:
            if e.origin is not v and e.destination is not v:
                new_E.append(e)
        self.E = new_E

        new_out = {}
        for vertex in self.outgoing:
            if vertex is not v:
                new_out[vertex] = []
                for e in self.outgoing[vertex]:
                    if e.origin is not v and e.destination is not v:
                        new_out[vertex].append(e)

        self.outgoing = new_out

        if self.directed:
            new_in = {}
            for vertex in self.incoming:
                if vertex is not v:
                    new_in[vertex] = []
                    for e in self.incoming[vertex]:
                        if e.origin is not v and e.destination is not v:
                            new_in[vertex].append(e)

            self.incoming = new_in

    def dfs(self, u, discovered=None):                     # O(n + m)
        """Returns dict vertex -> discovery edge (dict order = visit order)."""
        if discovered is None:
            discovered = {u: None}
        for e in self.incident_edges(u):
            v = e.opposite(u)
            if v not in discovered:
                discovered[v] = e
                self.dfs(v, discovered)
        return discovered

    def bfs(self, s):                                      # O(n + m)
        """Returns dict vertex -> discovery edge (dict order = visit order)."""
        discovered = {s: None}
        level = [s]
        while len(level) > 0:
            next_level = []
            for u in level:
                for e in self.incident_edges(u):
                    v = e.opposite(u)
                    if v not in discovered:
                        discovered[v] = e
                        next_level.append(v)
            level = next_level
        return discovered

    def prim_mst(self, s):                                 # O((n + m) log n)
        d = {}
        connect = {}                                       # vertex -> edge into tree
        pq = PriorityQueue()
        locators = {}
        for v in self.vertices():
            d[v] = 0 if v is s else float('inf')
            locators[v] = pq.add(d[v], v)
        tree = []
        while not pq.is_empty():
            key, u = pq.remove_min()
            new_locators = {}
            for vertex in locators:
                if vertex is not u:
                     new_locators[vertex] = locators[vertex]
            locators = new_locators            
            if u in connect:
                tree.append(connect[u])
            for e in self.incident_edges(u):
                v = e.opposite(u)
                if v in locators and e.element() < d[v]:
                    d[v] = e.element()
                    connect[v] = e
                    pq.update(locators[v], d[v], v)        # decrease-key
        return tree

    def dijkstra(self, s):                                 # O((n + m) log n)
        """Returns (dist, parent): parent[v] = edge on shortest path into v."""
        dist = {}
        parent = {s: None}
        pq = PriorityQueue()
        locators = {}
        for v in self.vertices():
            dist[v] = 0 if v is s else float('inf')
            locators[v] = pq.add(dist[v], v)
        while not pq.is_empty():
            key, u = pq.remove_min()
            new_locators = {}
            for vertex in locators:
                if vertex is not u:
                    new_locators[vertex] = locators[vertex]
            locators = new_locators   
            for e in self.incident_edges(u):
                v = e.opposite(u)
                if v in locators and dist[u] + e.element() < dist[v]:   # relax
                    dist[v] = dist[u] + e.element()
                    parent[v] = e
                    pq.update(locators[v], dist[v], v)
        return dist, parent
