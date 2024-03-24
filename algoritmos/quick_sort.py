# Quick Sort: Pick an element as pivot and partition the given array around the picked pivot
def quick_sort(arr):
    # TODO: Count the number of steps
    steps = 0
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    # TODO: Look for a way for returning the number of steps
    return quick_sort(left) + middle + quick_sort(right)