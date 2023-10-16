class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.time_compare = 0

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, vertex):
        self.queue.append(vertex)

    def dequeue(self):
        if self.is_empty():
            return None
        min_distance = float('inf')
        min_index = -1

        # Find the vertex with the minimum distance in the array
        for i, vertex in enumerate(self.queue):
            if vertex.distance < min_distance:
                min_distance = vertex.distance
                min_index = i
                self.time_compare += 1
        # ans_vertex = self.queue[min_index]
        # self.queue = self.queue.remove()

        if min_index != -1:
            return self.queue.pop(min_index)

    def decrease_key(self, vertex, new_distance):
        for v in self.queue:
            if v == vertex:
                v.distance = new_distance
                break
        

    def contains(self, vertex):
        return vertex in self.queue