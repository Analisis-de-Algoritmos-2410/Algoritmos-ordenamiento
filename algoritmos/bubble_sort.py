# Bubble Sort: Compare each pair of adjacent elements and swap them if they are in the wrong order
def bubble_sort(arr):
    n = len(arr)
    steps = 0
    for i in range(n):
        for j in range(0, n-i-1):
            steps += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                steps += 1
    return arr, steps
