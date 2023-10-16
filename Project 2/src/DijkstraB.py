# Example usage:
from GraphGeneratorB import GraphGeneratorB
from VerticeEdgeb import Graph
from HeapQueue import PriorityQueue

class DijkstraB:
    def dijkstra(graph, vertices, source_vertex):

        source_vertex.distance = 0  # Initialize the source vertex's distance to 0

        priority_queue = PriorityQueue()

        for vertex in vertices:
            priority_queue.enqueue(vertex)

        while not priority_queue.is_empty():
            current_vertex = priority_queue.dequeue()

            # Explore neighbors of the current vertex
            if current_vertex.vertex_id in graph.edges:
                for neighbor, weight in graph.edges[current_vertex.vertex_id]:
                    new_distance = current_vertex.distance + weight
                    if new_distance < neighbor.distance:
                        neighbor.distance = new_distance
                        neighbor.predecessor = current_vertex
                        priority_queue.decrease_key(neighbor, new_distance)

        print("Time of compare:", priority_queue.time_compare)
        return priority_queue.time_compare


# Create a random graph with 5 vertices and 7 edges
num_vertices = 20
num_edges = 40
vertices, edges = GraphGeneratorB.generate_random_graph(num_vertices, num_edges)

# Create a graph instance
graph = Graph()

# Add vertices to the graph
for vertex in vertices:
    graph.add_vertex(vertex)

# Add edges to the graph
for edge in edges:
    graph.add_edge(edge.start_vertex, edge.end_vertex, edge.weight)

# Perform Dijkstra's algorithm starting from the first vertex
source_vertex = vertices[0]

# Perform Dijkstra's algorithm starting from the first vertex
DijkstraB.dijkstra(graph, vertices, source_vertex)

# Print shortest paths from the first vertex to all other vertices
for vertex in vertices[1:]:
    print(f"Shortest path to {vertex.label}:")
    while vertex is not None:
        print(vertex.label, end=" -> ")
        print("Distance:", vertex.distance)
        vertex = vertex.predecessor