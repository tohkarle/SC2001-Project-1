class Vertex:
    def __init__(self, vertex_id, label):
        self.vertex_id = vertex_id  # Unique identifier for the vertex
        self.label = label  # Label or name for the vertex
        self.distance = float('inf')  # Initialize distance to infinity
        self.predecessor = None  # Predecessor vertex in the shortest path

    def __lt__(self, other):
        return self.distance < other.distance

class Edge:
    def __init__(self, start_vertex, end_vertex, weight):
        self.start_vertex = start_vertex  # Starting vertex of the edge
        self.end_vertex = end_vertex  # Ending vertex of the edge
        self.weight = weight  # Weight (cost) of the edge

# Create vertices
vertex_A = Vertex(0, 'A')
vertex_B = Vertex(1, 'B')
vertex_C = Vertex(2, 'C')

# Create edges and initialize the adjacency matrix
edges = [
    Edge(vertex_A, vertex_B, 4),
    Edge(vertex_A, vertex_C, 1),
    Edge(vertex_B, vertex_C, 2),
    # Add more edges as needed
]

# Initialize the adjacency matrix (assuming a 3x3 matrix for this example)
adjacency_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Populate the adjacency matrix based on the edges
for edge in edges:
    start_id = edge.start_vertex.vertex_id
    end_id = edge.end_vertex.vertex_id
    adjacency_matrix[start_id][end_id] = edge.weight

# Now, you have a graph represented using vertices and an adjacency matrix.