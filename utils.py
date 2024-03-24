
from matplotlib import pyplot as plt
import pandas as pd
import time

# Function to time the execution of a function
def time_function(func, arr):
    start = time.perf_counter()
    arr, steps = func(arr)
    final = time.perf_counter()
    return final-start, steps

# Function to plot a dictionary
def plot_dict(dictionary, title, xlabel, ylabel):
    df = pd.DataFrame(dictionary)
    df.index.name = 'n'
    df.reset_index(inplace=True)

    for key in dictionary:
        plt.plot(df['n'], df[key], label=key)

    plt.legend()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

# Function to print a polynomial
def print_polynomial(coefs):
    n = len(coefs)
    poly_str = ""
    for i in range(n):
        coef = round(coefs[i], 3)
        if i == 0:
            poly_str += str(coef)
        elif i == 1:
            poly_str += " + " + str(coef) + "n"
        else:
            poly_str += " + " + str(coef) + "n^" + str(i)
    return poly_str