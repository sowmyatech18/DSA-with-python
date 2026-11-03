# Adjacency Matrix graph: n x n matrix, A[i][j] = edge from vertex i to j or None
# (best: dense graph; get_edge is O(1), neighbours cost O(n), memory O(n^2))
from priority_queue import PriorityQueue


class AdjacencyMatrixGraph:
    class Vertex:
        def __init__(self, x, index):
            self.elem = x
            self.index = index                             # row/column in A

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
        self.V = []                                        # index -> vertex
        self.A = []                                        # the matrix
        self.m = 0

    def is_directed(self):
        return self.directed

    def vertex_count(self):
        return len(self.V)

    def vertices(self):
        return self.V

    def edge_count(self):
        return self.m

    def edges(self):                                       # O(n^2)
        result = []
        n = len(self.V)
        for i in range(n):
            start = 0 if self.directed else i              # undirected: upper half
            for j in range(start, n):
                if self.A[i][j] is not None:
                    result.append(self.A[i][j])
        return result

    def get_edge(self, u, v):                              # O(1)
        return self.A[u.index][v.index]

    def degree(self, v, outgoing=True):                    # O(n)
        count = 0
        for j in range(len(self.V)):
            e = self.A[v.index][j] if outgoing else self.A[j][v.index]
            if e is not None:
                count += 1
        return count

    def incident_edges(self, v, outgoing=True):            # O(n)
        result = []
        for j in range(len(self.V)):
            e = self.A[v.index][j] if outgoing else self.A[j][v.index]
            if e is not None:
                result.append(e)
        return result

    def insert_vertex(self, x=None):                       # O(n)
        v = self.Vertex(x, len(self.V))
        self.V.append(v)
        for row in self.A:
            row.append(None)                               # new column
        self.A.append([None] * len(self.V))                # new row
        return v

    def insert_edge(self, u, v, x=None):                   # O(1)
        if self.A[u.index][v.index] is not None:
            raise ValueError('u and v are already adjacent')
        e = self.Edge(u, v, x)
        self.A[u.index][v.index] = e
        if not self.directed:
            self.A[v.index][u.index] = e
        self.m += 1
        return e

    def remove_edge(self, e):                              # O(1)
        u, v = e.endpoints()
        self.A[u.index][v.index] = None
        if not self.directed:
            self.A[v.index][u.index] = None
        self.m -= 1

    def remove_vertex(self, v):                            # O(n^2)
        i = v.index
        n = len(self.V)
        for j in range(n):                                 # count edges being lost
            if self.A[i][j] is not None:
                self.m -= 1
            if self.directed and j != i and self.A[j][i] is not None:
                self.m -= 1
        del self.A[i]                                      # drop row i
        for row in self.A:
            del row[i]                                     # drop column i
        del self.V[i]
        for k in range(i, len(self.V)):                    # renumber the rest
            self.V[k].index = k

    def dfs(self, u, discovered=None):                     # O(n^2)
        """Returns dict vertex -> discovery edge (dict order = visit order)."""
        if discovered is None:
            discovered = {u: None}
        for e in self.incident_edges(u):
            v = e.opposite(u)
            if v not in discovered:
                discovered[v] = e
                self.dfs(v, discovered)
        return discovered

    def bfs(self, s):                                      # O(n^2)
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

    def prim_mst(self, s):                                 # O(n^2 + m log n)
        d = {}
        connect = {}
        pq = PriorityQueue()
        locators = {}
        for v in self.V:
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
            for j in range(len(self.V)):                   # scan row of u
                e = self.A[u.index][j]
                if e is None:
                    continue
                v = self.V[j]
                if v in locators and e.element() < d[v]:
                    d[v] = e.element()
                    connect[v] = e
                    pq.update(locators[v], d[v], v)        # decrease-key
        return tree

    def dijkstra(self, s):                                 # O(n^2 + m log n)
        """Returns (dist, parent): parent[v] = edge on shortest path into v."""
        dist = {}
        parent = {s: None}
        pq = PriorityQueue()
        locators = {}
        for v in self.V:
            dist[v] = 0 if v is s else float('inf')
            locators[v] = pq.add(dist[v], v)
        while not pq.is_empty():
            key, u = pq.remove_min()
            del locators[u]
            for j in range(len(self.V)):                   # scan row of u
                e = self.A[u.index][j]
                if e is None:
                    continue
                v = self.V[j]
                if v in locators and dist[u] + e.element() < dist[v]:   # relax
                    dist[v] = dist[u] + e.element()
                    parent[v] = e
                    pq.update(locators[v], dist[v], v)
        return dist, parent
