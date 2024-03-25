from algoritmos.bubble_sort import bubble_sort
from algoritmos.selection_sort import selection_sort
from algoritmos.insertion_sort import insertion_sort
from algoritmos.merge_sort import merge_sort
from algoritmos.quick_sort import quick_sort
from testing.stress_testing import stress_testing

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
        'times avg': {key: [] for key in solutionsFunctions},
        'times best': {key: [] for key in solutionsFunctions},
        'times worst': {key: [] for key in solutionsFunctions},
        'steps avg': {key: [] for key in solutionsFunctions},
        'steps best': {key: [] for key in solutionsFunctions},
        'steps worst': {key: [] for key in solutionsFunctions},
        'coefs': {key: [] for key in solutionsFunctions}
    }

    # Generate random arrays of different sizes
    tams = range(10, 1000, 10)
    for n in tams:
        # Caso promedio
        arr = [random.randrange(-100, 100) for _ in range(n + 1)]

        # Peor de los casos
        reverseArray = arr.copy()
        reverseArray.sort(reverse=True)

        # Mejor de los casos
        sortedArray = arr.copy()
        sortedArray.sort()

        for key in solutionsFunctions:
            # Caso promedio
            time, steps = time_function(solutionsFunctions[key], arr)
            results['times avg'][key].append(time)
            results['steps avg'][key].append(steps)

            # Peor de los casos
            time, steps = time_function(solutionsFunctions[key], reverseArray)
            results['times worst'][key].append(time)
            results['steps worst'][key].append(steps)

            # Mejor de los casos
            time, steps = time_function(solutionsFunctions[key], sortedArray)
            results['times best'][key].append(time)
            results['steps best'][key].append(steps)

    # Create a DataFrame and plot the results for time
    plot_dict(results['times avg'], 'Execution times in average case', 'n', 'Time (s)')
    # Create a DataFrame and plot the results for steps
    plot_dict(results['steps avg'], 'Steps in Average case', 'n', 'Steps')

    plot_dict(results['times best'], 'Execution times in best case', 'n', 'Time (s)')
    plot_dict(results['steps best'], 'Steps in best case', 'n', 'Steps')

    plot_dict(results['times worst'], 'Execution times in worst case', 'n', 'Time (s)')
    plot_dict(results['steps worst'], 'Steps in worst case', 'n', 'Steps')

    # Calculate the coefficients of the time complexity
    print('-' * 50, 'Time complexity coefficients', '-' * 50, sep='\n')
    for key in solutionsFunctions:
        results['coefs'][key] = Polynomial.fit(tams, results['steps avg'][key], 2).convert().coef
        print(key, ':     \t T(n) = ', print_polynomial(results['coefs'][key]), sep='')

    print("\nExecuting stress testing for all algorithms")

    ok = True
    for fun in solutionsFunctions:
        if not stress_testing(solutionsFunctions[fun]):
            print(f"Test case failed in {fun}")
            ok = False
            break

    if ok:
        print("All algorithms pass 100 tests")


if __name__ == '__main__':
    main()
