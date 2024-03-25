# Merge Sort: Divide the array in two halves, sort the two halves and merge them
def merge_sort(arr):
    steps = 0
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        _, steps_l = merge_sort(L)
        _, steps_r = merge_sort(R)
        steps += steps_l + steps_r + 5  # 5 steps for the merge

        # Merge
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            steps += 4  # 4 steps for the comparison and the assignment
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            steps += 3  # 3 steps for the assignment
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            steps += 3  # 3 steps for the assignment

    return arr, steps
