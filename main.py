from algoritmos.bubble_sort import bubble_sort
from algoritmos.selection_sort import selection_sort
from algoritmos.insertion_sort import insertion_sort
from algoritmos.merge_sort import merge_sort
from algoritmos.quick_sort import quick_sort

from matplotlib import pyplot as plt
import random
import pandas as pd
import time

solutionsFunctions = {
    'Bubble Sort': bubble_sort,
    'Selection Sort': selection_sort,
    'Insertion Sort': insertion_sort,
    'Merge Sort': merge_sort,
    'Quick Sort': quick_sort
}

# Function to time the execution of a function
def time_function(func, arr):
    start = time.perf_counter()
    func(arr)
    final = time.perf_counter()
    return final-start

def main():
    # Time for each algorithm
    time = {
        'Bubble Sort': [],
        'Selection Sort': [],
        'Insertion Sort': [],
        'Merge Sort': [],
        'Quick Sort': []
    }

    # Steps for each algorithm
    steps = {
        'Bubble Sort': [],
        'Selection Sort': [],
        'Insertion Sort': [],
        'Merge Sort': [],
        'Quick Sort': []
    }

    # Generate random arrays of different sizes
    for n in range(10, 10000, 100):
        arr = [random.randrange(-100, 100) for _ in range(n+1)]
        for key in solutionsFunctions:
            time[key].append(time_function(solutionsFunctions[key], arr))

    # Create a DataFrame and plot the results
    df = pd.DataFrame(time)
    df.index.name = 'n'
    df.reset_index(inplace=True)

    for key in solutionsFunctions:
        plt.plot(df['n'], df[key], label=key)
    
    plt.legend()
    plt.xlabel('n')
    plt.ylabel('Time (s)')
    plt.title('Execution times')
    plt.show()



if __name__ == '__main__':
    main()