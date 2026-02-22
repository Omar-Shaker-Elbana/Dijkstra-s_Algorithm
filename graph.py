class Graph:
    def __init__(self) -> None:
        self.graph = {}
        self.amount = 0

    def add_vertex(self, value):
        if value not in self.graph:
            self.graph[value] = []
            self.amount += 1

    def _set_edge(self, u, v, w):
        """
        Ensure (u -> v) exists with weight w.
        If it exists, update weight; if not, append.
        """
        adj = self.graph[u]
        for pair in adj:
            if pair[0] == v:
                pair[1] = w
                return
        adj.append([v, w])

    def add_edge(self, vertex1, vertex2, weight):
        # Undirected: store both directions
        if vertex1 in self.graph and vertex2 in self.graph:
            self._set_edge(vertex1, vertex2, weight)
            self._set_edge(vertex2, vertex1, weight)

    def remove_vertex(self, value):
        if value in self.graph:
            # Remove any edges pointing to `value`
            for u in list(self.graph.keys()):
                if u == value:
                    continue
                self.graph[u] = [pair for pair in self.graph[u] if pair[0] != value]

            # Now remove the vertex itself
            del self.graph[value]
            self.amount -= 1

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            # Remove vertex2 from vertex1's adjacency
            self.graph[vertex1] = [pair for pair in self.graph[vertex1] if pair[0] != vertex2]
            # Remove vertex1 from vertex2's adjacency
            self.graph[vertex2] = [pair for pair in self.graph[vertex2] if pair[0] != vertex1]

    def update_vertex(self, old, new):
        """
        Rename vertex `old` to `new` while keeping edges intact.
        Enforces uniqueness: raises ValueError if `new` already exists.
        """
        if old not in self.graph:
            return
        if new in self.graph:
            raise ValueError(f"Vertex '{new}' already exists. Vertex names must be unique.")

        # Move adjacency list from old -> new
        self.graph[new] = self.graph.pop(old)

        # For every neighbor that pointed to `old`, make it point to `new`
        for u, adj in self.graph.items():
            for i in range(len(adj)):
                if adj[i][0] == old:
                    adj[i][0] = new

