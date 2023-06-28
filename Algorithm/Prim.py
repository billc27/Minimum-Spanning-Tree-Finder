class Prim:
    def __init__(self, parse):
        self.vertices = parse.getRow()
        self.graph = parse.getGraph()
        self.path = []
        self.distance = 0

    def getPath(self):
        return self.path
    
    def getDistance(self):
        return self.distance

    # Find the vertex with the minimum distance value
    def min_key(self, keys, mst_sets):
        min_index = -1
        min_value = float('inf')
        for v in range(self.vertices):
            if keys[v] < min_value and not mst_sets[v]:
                min_value = keys[v]
                min_index = v
        return min_index

    # Construct MST using Prim Algorithm
    def mst_prim(self):
        keys = [float('inf')] * self.vertices
        parent = [-1] * self.vertices

        keys[0] = 0
        mst_sets = [False] * self.vertices
        
        parent[0] = -1
        for i in range(self.vertices):
            u = self.min_key(keys, mst_sets) # Pick the minimum distance vertex
            mst_sets[u] = True # Put the vertex in the shortest path tree
            for v in range(self.vertices):
                if self.graph[u][v] > 0 and not mst_sets[v] and self.graph[u][v] < keys[v]:
                    keys[v] = self.graph[u][v]
                    parent[v] = u

        # Solution
        for i in range(1, self.vertices):
            self.path.append([parent[i], i, self.graph[i][parent[i]]])
            self.distance += self.graph[i][parent[i]]

        return parent