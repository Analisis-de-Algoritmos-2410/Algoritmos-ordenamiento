from algoritmos.bubble_sort import bubble_sort
from algoritmos.selection_sort import selection_sort
from algoritmos.insertion_sort import insertion_sort
from algoritmos.merge_sort import merge_sort
from algoritmos.quick_sort import quick_sort

from utils import time_function, plot_dict, print_polynomial
from numpy.polynomial.polynomial import Polynomial
import random

solutionsFunctions = {
    'Bubble Sort': bubble_sort,
    'Selection Sort': selection_sort,
    'Insertion Sort': insertion_sort,
    'Merge Sort': merge_sort,
    'Quick Sort': quick_sort
}

def main():
    results = {
        'times' : {key: [] for key in solutionsFunctions},
        'steps' : {key: [] for key in solutionsFunctions},
        'coefs' : {key: [] for key in solutionsFunctions}
    }

    # Generate random arrays of different sizes
    tams = range(10, 1000, 10)
    for n in tams:
        arr = [random.randrange(-100, 100) for _ in range(n+1)]
        for key in solutionsFunctions:
            time, steps = time_function(solutionsFunctions[key], arr)
            results['times'][key].append(time)
            results['steps'][key].append(steps)

    # Create a DataFrame and plot the results for time
    plot_dict(results['times'], 'Execution times', 'n', 'Time (s)')
    # Create a DataFrame and plot the results for steps
    plot_dict(results['steps'], 'Steps', 'n', 'Steps')

    # Calculate the coefficients of the time complexity
    print('-'*50, 'Time complexity coefficients', '-'*50, sep='\n')
    for key in solutionsFunctions:
        results['coefs'][key] = Polynomial.fit(tams, results['steps'][key], 2).convert().coef
        print(key, ':     \t T(n) = ', print_polynomial(results['coefs'][key]), sep='')


if __name__ == '__main__':
    main()
