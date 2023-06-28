class Kruskal:
    def __init__(self, parse):
        self.vertices = parse.getRow()
        self.graph = parse.getGraph()
        self.path = []
        self.distance = 0

    def getPath(self):
        return self.path
    
    def getDistance(self):
        return self.distance

    # Parse adjacency matrix into [[src, dest, weight], ...]
    def parse_adj_matrix(adj_matrix):
        vertices_num = len(adj_matrix)
        edges = []
        for i in range(vertices_num):
            for j in range(i + 1, vertices_num):
                weight = adj_matrix[i][j]
                if weight != 0:
                    edges.append([i, j, weight])
        return edges
 
    # Find set of an element i using path compression
    def find(self, parent, i):
        if parent[i] != i:
            # Reassignment of node's parent to root node as path compression requires
            parent[i] = self.find(parent, parent[i])
        return parent[i]
 
    def union(self, parent, rank, x, y):
        # Attach smaller rank tree under root of high rank tree
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1
 
    def mst_kruskal(self):
        # Index for sorted edges
        i = 0
 
        # Index for the path result
        j = 0
 
        # Sort all the edges in non-decreasing order based on their weight
        self.graph = sorted(self.graph,
                            key=lambda item: item[2])
 
        parent = []
        rank = []
 
        # Create V subsets with single elements
        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)
 
        # The number of edges to be taken is less than V-1
        while j < self.vertices - 1:
            # Pick the smallest edge and increment the index
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
 
            # If including this edge doesn't produce a cycle, include it in path result and increment the path result index for the next edge
            if x != y:
                j = j + 1
                self.path.append([u, v, w])
                self.union(parent, rank, x, y)

            # If not, discard the edge
 
        # Calculate the distance
        for u, v, weight in self.path:
            self.distance += weight
