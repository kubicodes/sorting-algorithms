from constants import SORTING_ALGORITHMS

def convertStrArrToIntArr(arr):
    for index, value in enumerate(arr):
        try:
            arr[index] = int(value)
        except:
            print("Only Integer values are allowed.")
            exit(1)
    
    return arr

if __name__ == "__main__":
    inputStr = input("Please provide numbers separated by a space you want to sort: ")
    arr = convertStrArrToIntArr(inputStr.split())

    sortingAlgorithmChoice = input(f'Which Sorting Algorithm do you want to use?, You can use between: {", ".join(SORTING_ALGORITHMS.keys())} \n')

    if not sortingAlgorithmChoice in SORTING_ALGORITHMS:
        print(f'Sorting algortihm {sortingAlgorithmChoice} is not an option')
        exit(1)
    
    sorter = SORTING_ALGORITHMS[sortingAlgorithmChoice]
    result = sorter(arr).sort()

    print("Succesfully sorted the list")
    print(result)

