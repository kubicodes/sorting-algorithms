class MergeSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        self._mergeSort(self.arr)
        return self.arr

    def _mergeSort(self, arr):
        if len(arr) > 1:
            middleIndex = len(arr) // 2
            leftArr = arr[:middleIndex]
            rightArr = arr[middleIndex:]

            self._mergeSort(leftArr)
            self._mergeSort(rightArr)

            self._merge(arr, leftArr, rightArr)

    def _merge(self, arr, leftArr, rightArr):
        indexLeftArr = 0
        indexRightArr = 0
        sortedIndex = 0

        while indexLeftArr < len(leftArr) and indexRightArr < len(rightArr):
            if leftArr[indexLeftArr] < rightArr[indexRightArr]:
                arr[sortedIndex] = leftArr[indexLeftArr]
                indexLeftArr += 1
            else:
                arr[sortedIndex] = rightArr[indexRightArr]
                indexRightArr += 1

            sortedIndex += 1

        # left overs when arrays were not equally long
        while indexLeftArr < len(leftArr):
            arr[sortedIndex] = leftArr[indexLeftArr]
            indexLeftArr += 1
            sortedIndex += 1

        while indexRightArr < len(rightArr):
            arr[sortedIndex] = rightArr[indexRightArr]
            indexRightArr += 1
            sortedIndex += 1

