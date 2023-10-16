class Vertex:
    def __init__(self, vertex_id, label):
        self.vertex_id = vertex_id
        self.label = label
        self.distance = float('inf')  # Initialize distance to infinity
        self.predecessor = None  # Predecessor vertex in the shortest path

    def __lt__(self, other):
        return self.distance < other.distance

class Edge:
    def __init__(self, start_vertex, end_vertex, weight):
        self.start_vertex = start_vertex  # Source vertex of the edge
        self.end_vertex = end_vertex  # Target vertex of the edge
        self.weight = weight  # Weight (cost) of the edge

class Graph:
    def __init__(self):
        self.vertices = {}  # Dictionary to store vertices by their IDs
        self.edges = {}  # Dictionary to store edges by source vertex IDs

    def add_vertex(self, vertex):
        self.vertices[vertex.vertex_id] = vertex

    def add_edge(self, source_vertex, target_vertex, weight):
        if source_vertex.vertex_id not in self.edges:
            self.edges[source_vertex.vertex_id] = []
        self.edges[source_vertex.vertex_id].append((target_vertex, weight))