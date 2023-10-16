class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.vertex_indices = {}  # A dictionary to track vertex indices in the heap
        self.time_compare = 0

    def is_empty(self):
        return len(self.heap) == 0

    def enqueue(self, vertex):
        self.heap.append(vertex)
        self.vertex_indices[vertex] = len(self.heap) - 1
        self._bubble_up(len(self.heap) - 1)

    def dequeue(self):
        if not self.is_empty():
            min_vertex = self.heap[0]
            last_vertex = self.heap.pop()
            if len(self.heap) > 0:
                self.heap[0] = last_vertex
                self.vertex_indices[last_vertex] = 0
                self._bubble_down(0)
            del self.vertex_indices[min_vertex]
            return min_vertex

    def decrease_key(self, vertex, new_distance):
        if new_distance < vertex.distance:
            vertex.distance = new_distance
            index = self.vertex_indices[vertex]
            self._bubble_up(index)

    def contains(self, vertex):
        return vertex in self.vertex_indices

    def _bubble_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2

            self.time_compare += 1

            if self.heap[index] < self.heap[parent_index]:
                # Swap the vertices
                self._swap(index, parent_index)
                index = parent_index
            else:
                break

    def _bubble_down(self, index):
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index

            self.time_compare += 1

            if (left_child_index < len(self.heap) and
                    self.heap[left_child_index] < self.heap[smallest]):
                smallest = left_child_index
            if (right_child_index < len(self.heap) and
                    self.heap[right_child_index] < self.heap[smallest]):
                smallest = right_child_index

            if smallest != index:
                # Swap the vertices
                self._swap(index, smallest)
                index = smallest
            else:
                break

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.vertex_indices[self.heap[i]] = i
        self.vertex_indices[self.heap[j]] = j