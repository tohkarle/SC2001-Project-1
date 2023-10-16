import random
from VerticeEdgeA import Vertex
from VerticeEdgeA import Edge

class GraphGenerator:
    @staticmethod
    def generate_random_graph(num_vertices, num_edges):
        if num_vertices < 2 or num_edges < num_vertices - 1 or num_edges > num_vertices * (num_vertices - 1) // 2:
            raise ValueError("Invalid input parameters")

        # Create vertices
        vertices = [Vertex(i, f'V{i}') for i in range(num_vertices)]

        # Create a list of all possible edges
        all_possible_edges = [(i, j) for i in range(num_vertices) for j in range(i + 1, num_vertices)]

        # Randomly shuffle the list to select edges
        random.shuffle(all_possible_edges)

        # Create edges with random weights
        edges = []
        for i in range(num_edges):
            start_vertex_index, end_vertex_index = all_possible_edges[i]
            weight = random.randint(1, 100)  # Adjust the range as needed
            edges.append(Edge(vertices[start_vertex_index], vertices[end_vertex_index], weight))

        return vertices, edges