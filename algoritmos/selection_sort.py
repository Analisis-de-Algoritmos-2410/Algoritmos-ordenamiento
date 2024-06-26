# Selection Sort: Find the minimum element in unsorted array and swap it with element at the beginning
def selection_sort(arr):
    n = len(arr)
    steps = 0
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            steps += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        steps += 1
    return arr, steps