class Parser:
    def __init__(self, filePath):
        self.row = -1
        self.col = -1
        self.graph = []
        self.filePath = filePath

    def getRow(self):
        return self.row
    
    # Get the adjacency matrix
    def getGraph(self):
        return self.graph

    def isGraphSymmetric(self):
        i = 0
        if (self.row != self.col):
            return False
        else:
            for i in range(len(self.graph)):
                for j in range(i+1, len(self.graph[i])):
                    if self.graph[i][j] != self.graph[j][i]:
                        return False
            return True
        
    def parseFile(self): # Not checked if it is symmetric, just loads
        with open(self.filePath, 'r') as file:
            lines = file.readlines()

        for line in lines:
            row = [int(num) for num in line.split()]
            self.graph.append(row)
        
        if (self.isGraphSymmetric()):
            self.row = len(self.graph)
            if self.row > 0:
                self.col = len(self.graph[0])
        else:
            self.graph = []

    def print_graph(self):
        print(self.graph)

    

# Usage example
# graph = Parser("Helper/test.txt")
# graph.parseFile()
# graph.print_graph()
# print(graph.isGraphSymmetric())
