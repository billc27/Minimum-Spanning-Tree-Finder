
import networkx as nx
import matplotlib.pyplot as plt

class GraphVisualizer:
    def __init__(self, adjacency_matrix):
        self.adjacency_matrix = adjacency_matrix
        self.graph = nx.Graph()
        num_nodes = len(adjacency_matrix)
        
        # # Add the nodes to the graph
        for i in range (num_nodes):
            self.graph.add_node(f"{i+1}")

        # Add the edge and its weight to graph
        for i in range(num_nodes):
            for j in range(i, num_nodes):
                if (adjacency_matrix[i][j] != 0):
                    self.graph.add_edge(f"{i+1}", f"{j+1}", weight=adjacency_matrix[i][j])
                    self.graph.add_edge(f"{j+1}", f"{i+1}", weight=adjacency_matrix[j][i])


    def drawGraph(self):
        # Create the image of graph and save it
        edges = [(u, v) for (u, v, d) in self.graph.edges(data=True)]
        edge_labels = nx.get_edge_attributes(self.graph, "weight")
        try:
            pos = nx.planar_layout(self.graph)
        except:
            pos = nx.spring_layout(self.graph)

        nx.draw_networkx_nodes(self.graph, pos, node_size=350, node_color="#a7a374")
        nx.draw_networkx_labels(self.graph, pos, font_size=12, font_family="monospace")
        nx.draw_networkx_edges(self.graph, pos, edgelist=edges, width=2)

        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels, font_size=12, font_family="Times New Roman")

        ax = plt.gca()
        ax.margins(0.08)
        plt.axis("off")
        plt.tight_layout()
        plt.savefig("Assets/graph.png")
        plt.close("all")

    def transformResultPath(self, resultPath):
        edgeList = []
        for path in resultPath:
            src = path[0]
            dest = path[1]
            edgeList.append((f"{src + 1}", f"{dest + 1}"))
            edgeList.append((f"{dest + 1}", f"{src + 1}"))
        return edgeList

    def drawGraphResult(self, resultPath):
        # Get all the result edge
        resultEdge = self.transformResultPath(resultPath)

        # Create the image of graph and save it
        normalEdges = [(u, v) for (u, v, d) in self.graph.edges(data=True) if (u, v) not in resultEdge]
        resultEdges = [(u, v) for (u, v, d) in self.graph.edges(data=True) if (u, v) in resultEdge]
        edge_labels = nx.get_edge_attributes(self.graph, "weight")
        try:
            pos = nx.planar_layout(self.graph)
        except:
            pos = nx.spring_layout(self.graph)

        nx.draw_networkx_nodes(self.graph, pos, node_size=350, node_color="#a7a374")
        nx.draw_networkx_labels(self.graph, pos, font_size=12, font_family="monospace")
        nx.draw_networkx_edges(self.graph, pos, edgelist=normalEdges, width=2, edge_color="#000000")
        nx.draw_networkx_edges(self.graph, pos, edgelist=resultEdges, width=2, edge_color="#FF1100")

        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels, font_size=12, font_family="Times New Roman")

        ax = plt.gca()
        ax.margins(0.08)
        plt.axis("off")
        plt.tight_layout()
        plt.savefig("Assets/graph.png")
        plt.close("all")
