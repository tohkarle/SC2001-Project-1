from GraphGeneratorA import GraphGenerator
from PriorityQueue import PriorityQueue

class Dijkstra:
        
    def dijkstra(graph, vertices, source_vertex):
        # Initialize distances and predecessors
        for vertex in vertices:
            vertex.distance = float('inf')
            vertex.predecessor = None

        source_vertex.distance = 0

        # Create a priority queue
        priority_queue = PriorityQueue()

        # Enqueue all vertices into the priority queue
        for vertex in vertices:
            priority_queue.enqueue(vertex)

        while not priority_queue.is_empty():
            print(len(priority_queue.queue))
            current_vertex = priority_queue.dequeue()

            if current_vertex is None:
                break

            # print(current_vertex)
            # current_vertex = current_vertex_comp.vertex

            # Explore neighbors of the current vertex
            for neighbor_index, weight in enumerate(graph[int(current_vertex.label[1:])]):
                if weight > 0:  # There's an edge to the neighbor
                    neighbor = vertices[neighbor_index]

                    # Calculate the new distance
                    new_distance = current_vertex.distance + weight

                    if new_distance < neighbor.distance:
                        neighbor.distance = new_distance
                        neighbor.predecessor = current_vertex

                        # Update the priority queue with the decreased key
                        priority_queue.decrease_key(neighbor, new_distance)

        print("Time of comparison: ", priority_queue.time_compare)

    def print_shortest_path(destination_vertex):
        if destination_vertex.predecessor is not None:
            Dijkstra.print_shortest_path(destination_vertex.predecessor)
        print(destination_vertex.label)

# Example usage:
num_vertices = 20
num_edges = 40

# Generate a random graph
vertices, edges = GraphGenerator.generate_random_graph(num_vertices, num_edges)

# Convert the edges into an adjacency matrix
adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]
for edge in edges:
    adjacency_matrix[edge.start_vertex.vertex_id][edge.end_vertex.vertex_id] = edge.weight

# Perform Dijkstra's algorithm starting from the first vertex
Dijkstra.dijkstra(adjacency_matrix, vertices, vertices[0])

# Print shortest paths from the first vertex to all other vertices
for vertex in vertices[1:]:
    print(f"Shortest path to {vertex.label}:")
    Dijkstra.print_shortest_path(vertex)
    print(f"Distance: {vertex.distance}\n")
