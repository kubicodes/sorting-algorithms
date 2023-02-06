class HeapSort:
    def __init__(self, arr):
        self.arr = arr
    
    def sort(self):
        self._heapSort(self.arr)
        return self.arr
    
    def _heapSort(self, arr):
        n = len(arr)

        for i in range(n // 2, -1, -1):
            # Build max heap
            self._heapify(arr, n, i)

        for i in range(n - 1, 0, - 1):
            # Sort
            self._swap(arr, i, 0)
            self._heapify(arr, i, 0)
    
    def _heapify(self, arr, n, i):
        # find the largest element in the subtree
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] < arr[left]:
            largest = left
        
        if right < n and arr[largest] < arr[right]:
            largest = right
        
        if largest != i:
            self._swap(arr, i, largest)
            # recursively sort again
            self._heapify(arr, n, largest)
    
    def _swap(self, arr, i, k):
        temp = arr[i]
        arr[i] = arr[k]
        arr[k] = temp