import unittest


class MinHeap:

    def __init__(self):
        self.heap = []
    
    def insert(self, element):
        self.heap.append(element)
        
        index = len(self.heap) - 1
        parent_index = (index - 1) // 2
        while self.heap[index] < self.heap[parent_index] and index > 0:
            self._swap_indices(index, parent_index)
            index = parent_index
            parent_index = (parent_index - 1) // 2
    
    def size(self):
        return len(self.heap)

    def remove_smallest(self):
        if not self.heap:
            return None
        
        self._swap_indices(0, -1)
        to_return = self.heap.pop()
        self._min_heapify(0)
        return to_return

    def _min_heapify(self, node_index):
        left_child = 2 * node_index + 1
        right_child = 2 * node_index + 2

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[node_index]:
            smallest = left_child
        else:
            smallest = node_index
        
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child
        
        if smallest != node_index:
            self._swap_indices(smallest, node_index)
            self._min_heapify(smallest)
    
    def _swap_indices(self, index_a, index_b):
        temp = self.heap[index_a]
        self.heap[index_a] = self.heap[index_b]
        self.heap[index_b] = temp


class TestMinHeap(unittest.TestCase):
    def test_min_heap_0(self):
        source_array = [3, 5, 4, 2, 1, 87, 34, 4]            
        heap = MinHeap()
        for element in source_array:
            heap.insert(element)
        self.assertEqual(len(source_array), heap.size())

        for element in sorted(source_array):
            self.assertEqual(element, heap.remove_smallest())
        self.assertEqual(0, heap.size())
    
    def test_min_heap_1(self):
        source_array = [54, 23, 23, 3, 7, 5, 5, 5]            
        heap = MinHeap()
        for element in source_array:
            heap.insert(element)
        self.assertEqual(len(source_array), heap.size())

        for element in sorted(source_array):
            self.assertEqual(element, heap.remove_smallest())
        self.assertEqual(0, heap.size())

    def test_min_heap_remove_empty(self):
        heap = MinHeap()
        self.assertEqual(None, heap.remove_smallest())
        self.assertEqual(0, heap.size())

if __name__ == "__main__":
    unittest.main()
