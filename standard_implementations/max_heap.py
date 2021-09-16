import unittest


class MaxHeap:

    def __init__(self):
        self.heap = []
    
    def insert(self, element):
        self.heap.append(element)
        
        index = len(self.heap) - 1
        parent_index = (index - 1) // 2
        while self.heap[index] > self.heap[parent_index] and index > 0:
            self._swap_indices(index, parent_index)
            index = parent_index
            parent_index = (parent_index - 1) // 2
    
    def size(self):
        return len(self.heap)

    def remove_largest(self):
        if not self.heap:
            return None
        
        self._swap_indices(0, -1)
        to_return = self.heap.pop()
        self._max_heapify(0)
        return to_return

    def _max_heapify(self, node_index):
        left_child = 2 * node_index + 1
        right_child = 2 * node_index + 2

        if left_child < len(self.heap) and self.heap[left_child] > self.heap[node_index]:
            largest = left_child
        else:
            largest = node_index
        
        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            largest = right_child
        
        if largest != node_index:
            self._swap_indices(largest, node_index)
            self._max_heapify(largest)
    
    def _swap_indices(self, index_a, index_b):
        temp = self.heap[index_a]
        self.heap[index_a] = self.heap[index_b]
        self.heap[index_b] = temp


class TestMaxHeap(unittest.TestCase):
    def test_max_heap_0(self):
        source_array = [3, 5, 4, 2, 1, 87, 34, 4]            
        heap = MaxHeap()
        for element in source_array:
            heap.insert(element)
        self.assertEqual(len(source_array), heap.size())

        for element in reversed(sorted(source_array)):
            self.assertEqual(element, heap.remove_largest())
        self.assertEqual(0, heap.size())
    
    def test_max_heap_1(self):
        source_array = [54, 23, 23, 3, 7, 5, 5, 5]            
        heap = MaxHeap()
        for element in source_array:
            heap.insert(element)
        self.assertEqual(len(source_array), heap.size())

        for element in reversed(sorted(source_array)):
            self.assertEqual(element, heap.remove_largest())
        self.assertEqual(0, heap.size())

    def test_max_heap_remove_empty(self):
        heap = MaxHeap()
        self.assertEqual(None, heap.remove_largest())
        self.assertEqual(0, heap.size())

if __name__ == "__main__":
    unittest.main()
