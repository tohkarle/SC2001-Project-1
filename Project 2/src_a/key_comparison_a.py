class VertexDistanceKey:
    def __init__(self, vertex):
        self.vertex = vertex

    def __lt__(self, other):
        return self.vertex.distance < other.vertex.distance

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, vertex):
        self.queue.append(VertexDistanceKey(vertex))

    def dequeue(self):
        if self.is_empty():
            return None
        min_distance = float('inf')
        min_index = -1

        # Find the vertex with the minimum distance in the array
        for i, key in enumerate(self.queue):
            if key.vertex.distance < min_distance:
                min_distance = key.vertex.distance
                min_index = i

        if min_index != -1:
            return self.queue.pop(min_index).vertex

    def decrease_key(self, vertex, new_distance):
        for key in self.queue:
            if key.vertex == vertex:
                key.vertex.distance = new_distance
                break

    def contains(self, vertex):
        return any(key.vertex == vertex for key in self.queue)

class VertexDistanceKey:
    def __init__(self, vertex):
        self.vertex = vertex

    def __lt__(self, other):
        result = self.vertex.distance < other.vertex.distance
        if result:
            print(f"Comparing {self.vertex.label}({self.vertex.distance}) < {other.vertex.label}({other.vertex.distance})")
        return result

def dequeue(self):
    if self.is_empty():
        return None
    min_distance = float('inf')
    min_index = -1

    # Find the vertex with the minimum distance in the array
    for i, key in enumerate(self.queue):
        if key < min_distance:
            min_distance = key.vertex.distance
            min_index = i
            print(f"New minimum: {key.vertex.label}({key.vertex.distance})")

    if min_index != -1:
        return self.queue.pop(min_index).vertex