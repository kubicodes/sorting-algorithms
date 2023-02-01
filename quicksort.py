class QuickSort:
    def __init__(self, arr):
        self.arr = arr
    
    def sort(self):
        return self._quickSort(self.arr, 0, len(self.arr) - 1)

    def _quickSort(self, arr, leftPointer, rightPointer):
        pivotIndex = self._getPivotIndex(arr, leftPointer, rightPointer)

        if pivotIndex != -1:
            partionedIndex = self._partition(arr, leftPointer, rightPointer, arr[pivotIndex])
            self._quickSort(arr, leftPointer, partionedIndex - 1)
            self._quickSort(arr, partionedIndex, rightPointer)

        return arr
        
    def _partition(self, arr, leftPointer, rightPointer, pivotElement):
        while leftPointer < rightPointer:
            if arr[leftPointer] < pivotElement:
                leftPointer += 1
                continue
            
            if arr[rightPointer] >= pivotElement:
                rightPointer -= 1
                continue
            
            self._swap(arr, leftPointer, rightPointer)
        
        return leftPointer

    def _swap(self, arr, firstIndex, secondIndex):
        if len(arr) < 2:
            return arr

        temp = arr[firstIndex]
        arr[firstIndex] = arr[secondIndex] 
        arr[secondIndex] = temp

    def _getPivotIndex(self, arr, leftPointer, rightPointer):
        while leftPointer < rightPointer:
            if arr[leftPointer] == arr[leftPointer + 1]:
                leftPointer += 1
                continue
            
            if arr[leftPointer] < arr[rightPointer]:
                return leftPointer + 1

            if arr[leftPointer] > arr[rightPointer]:
                return leftPointer
            
        return -1