# Insertion Sort: Insert an element from unsorted array to its correct position in sorted array
def insertion_sort(arr):
    n = len(arr)
    steps = 0
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            steps += 2
        arr[j+1] = key
        steps += 1
    return arr, steps
