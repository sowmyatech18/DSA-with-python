# Edge List graph: a list of vertices + a list of edges (best: sparse graph,
# algorithms that sweep all edges -> Kruskal, Boruvka)
from dsu import DSU
from min_heap import MinHeap


class EdgeListGraph:
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

        def __repr__(self):
            return f"({self.origin}, {self.destination}, {self.elem})"

    def __init__(self, directed=False):
        self.directed = directed
        self.V = []
        self.E = []

    def is_directed(self):
        return self.directed

    def vertex_count(self):
        return len(self.V)

    def vertices(self):
        return self.V

    def edge_count(self):
        return len(self.E)

    def edges(self):
        return self.E

    def get_edge(self, u, v):                              # O(m)
        for e in self.E:
            if e.origin is u and e.destination is v:
                return e
            if not self.directed and e.origin is v and e.destination is u:
                return e
        return None

    def degree(self, v, outgoing=True):                    # O(m)
        count = 0
        for e in self.E:
            if self.directed:
                if (outgoing and e.origin is v) or (not outgoing and e.destination is v):
                    count += 1
            elif e.origin is v or e.destination is v:
                count += 1
        return count

    def incident_edges(self, v, outgoing=True):            # O(m)
        result = []
        for e in self.E:
            if self.directed:
                if (outgoing and e.origin is v) or (not outgoing and e.destination is v):
                    result.append(e)
            elif e.origin is v or e.destination is v:
                result.append(e)
        return result

    def insert_vertex(self, x=None):                       # O(1)
        v = self.Vertex(x)
        self.V.append(v)
        return v

    def insert_edge(self, u, v, x=None):                   # O(1) (+ O(m) check)
        if self.get_edge(u, v) is not None:
            raise ValueError('u and v are already adjacent')
        e = self.Edge(u, v, x)
        self.E.append(e)
        return e

    def remove_edge(self, e):                              # O(m)
        new_E = []
        for edge in self.E:
            if edge is not e:
                new_E.append(edge)
        self.E = new_E

    def remove_vertex(self, v):                            # O(n + m)
        new_E = []
        for e in self.E:
            if e.origin is not v and e.destination is not v:
                new_E.append(e)
        self.E = new_E
        new_V=[]
        for vertex in self.V:
            if vertex is not v:
                new_V.append(vertex)
        self.V=new_V

    def dfs(self, u, discovered=None):
        """Returns dict vertex -> discovery edge (dict order = visit order)."""
        if discovered is None:
            discovered = {u: None}
        for e in self.incident_edges(u):
            v = e.opposite(u)
            if v not in discovered:
                discovered[v] = e
                self.dfs(v, discovered)
        return discovered

    def bfs(self, s):
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

    def kruskal_mst(self):                                 # O(m log m)
        heap = MinHeap()
        for e in self.E:
            heap.push(e.element(), e)
        dsu = DSU()
        for v in self.V:
            dsu.make_set(v)
        tree = []
        while len(tree) < len(self.V) - 1 and not heap.is_empty():
            weight, e = heap.pop_min()
            u, v = e.endpoints()
            if dsu.union(u, v):                            # no cycle -> take it
                tree.append(e)
        return tree

    def boruvka_mst(self):                                 # O(m log n)
        dsu = DSU()
        for v in self.V:
            dsu.make_set(v)
        tree = []
        while True:
            cheapest = {}                                  # root -> cheapest edge out
            for i in range(len(self.E)):
                e = self.E[i]
                ru = dsu.find(e.origin)
                rv = dsu.find(e.destination)
                if ru == rv:
                    continue
                for r in (ru, rv):
                    # tie-break on (weight, index) so no cycle forms
                    if r not in cheapest or (e.element(), i) < cheapest[r][0]:
                        cheapest[r] = ((e.element(), i), e)
            if len(cheapest) == 0:
                break
            for key, e in cheapest.values():
                if dsu.union(e.origin, e.destination):
                    tree.append(e)
        return tree
