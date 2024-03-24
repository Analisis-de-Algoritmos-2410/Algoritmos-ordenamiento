# Quick Sort: Pick an element as pivot and partition the given array around the picked pivot
def quick_sort(arr):
    steps = 0

    if len(arr) <= 1:
        return arr, steps
    
    pivot = arr[len(arr) // 2]
    steps += 1 # 1 step for the pivot
    left = [x for x in arr if x < pivot]
    steps += len(left) # 1 step for each element in the left array
    middle = [x for x in arr if x == pivot]
    steps += len(middle) # 1 step for each element in the middle array
    right = [x for x in arr if x > pivot]
    steps += len(right) # 1 step for each element in the right array

    l_arr, steps_l = quick_sort(left)
    r_arr, steps_r = quick_sort(right)
    steps += steps_l + steps_r + 1 # 1 step for the pivot

    return l_arr + middle + r_arr, steps
