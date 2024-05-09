class Graph:
    def __init__(self, vertices):
        pass
        self.V = vertices
        self.graph = [[]]

    # Check if the colored vertex is safe or not
    def is_safe(self, v, colour, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and colour[i] == c:
                return False
        return True

    # Color vertices using greedy algorithm
    def greedy_coloring(self):
        result = [-1] * self.V
        result[0] = 0  # Color the first vertex with the first color

        # Assign colors to remaining V-1 vertices
        for u in range(1, self.V):
            available = [True] * self.V

            for i in range(self.V):
                if self.graph[u][i] == 1 and result[i] != -1:
                    available[result[i]] = False

            # Find the first available color
            for c in range(self.V):
                if available[c]:
                    result[u] = c
                    break

        # Print the result
        print("Vertex   Color")
        for u in range(self.V):
            print(f"   {u}   -->   {result[u]}")



g = Graph(5)
g.graph = [
        [0, 1, 1, 1, 0],
        [1, 0, 1, 0, 1],
        [1, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0]
    ]
    
    # Color the graph
g.greedy_coloring()
