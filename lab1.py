import numpy as np
import heapq

class Graph:
    def __init__(self, adjacency_matrix=None, adjacency_list=None):
        if adjacency_matrix is not None:
            self.graph_type = 'matrix'
            self.matrix = np.array(adjacency_matrix)
            self.n = self.matrix.shape[0]
        elif adjacency_list is not None:
            self.graph_type = 'list'
            self.adj_list = adjacency_list
            self.n = len(adjacency_list)
        else:
            raise ValueError("Граф задаётся матрицей смежности или списком смежных вершин")

    def get_neighbors(self, node):
        if self.graph_type == 'matrix':
            neighbors = []
            for neighbor, weight in enumerate(self.matrix[node]):
                if weight > 0:
                    neighbors.append((neighbor, weight))
            return neighbors
        else:
            return self.adj_list[node]

    def dijkstra(self, start):
        distances = [float('inf')] * self.n
        distances[start] = 0
        visited = [False] * self.n
        heap = [(0, start)]

        while heap:
            current_dist, current_node = heapq.heappop(heap)
            if visited[current_node]:
                continue
            visited[current_node] = True

            for neighbor, weight in self.get_neighbors(current_node):
                if not visited[neighbor]:
                    new_dist = current_dist + weight
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        heapq.heappush(heap, (new_dist, neighbor))
        
        return distances



# Использование

adj_matrix = [
    [0,  7,  9,  0,  0, 14],
    [7,  0, 10, 15, 0,  0],
    [9, 10, 0, 11, 0,  2],
    [0, 15, 11, 0, 6,  0],
    [0,  0,  0, 6, 0,  9],
    [14, 0,  2, 0, 9,  0]
]

g = Graph(adjacency_matrix=adj_matrix)
start_vertex = 0
distances = g.dijkstra(start_vertex)
print(f"Кратчайшие расстояния от вершины {start_vertex}: {distances}")
