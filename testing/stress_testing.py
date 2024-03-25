import random


def stress_testing(func):
    for _ in range(0, 100):
        n = random.randrange(0, 20)
        arr = [random.randrange(-100, 100) for _ in range(n + 1)]
        result, steps = func(arr)
        arr.sort()
        for i in range(0, n):
            if arr[i] != result[i]:
                return False
    return True
