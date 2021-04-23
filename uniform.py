#!/usr/bin/env python

"""
uniform.py

Generates an array of random numbers in a uniform generator with values between 0 and 1, inputs each numbers' value into
a mathematical formula, examines the numbers and plots them.

* Change the quantity variable in the main function to generate more or fewer numbers
* Change the mu variable in the main function to alter the curve of the plot

This file can also be imported as a module and contains the following functions:

    * generate_random_numbers_uniform - Generates an array of random numbers between 0 and 1
    * iterate_formula - Iterates a given array of numbers through a mathematical formula
    * plot_histogram - Plots a histogram
    * examine_data - Examines a data array
"""

__author__ = "Frederik Bußmann"

import matplotlib.pyplot as plt

import numpy as np


def generate_random_numbers_uniform(size):
    """
    Generates an array of random numbers between 0 and 1.

    Parameters
    ----------
    size : int
        The quantity of numbers to generate, i.e. the size of the array

    Returns
    -------
    float[]
        The array of generated random numbers
    """

    print("Generating array of " + str(size) + " random numbers between 0 and 1...\n")

    numbers = np.random.uniform(0., 1., size)

    print("Done.\n\n")

    return numbers


def iterate_formula(numbers, mu):
    """
    Iterates through a set of numbers and applies the mathematical formula f(p) = -(1 / mu) * ln(p) for each number.

    Parameters
    ----------
    numbers : float[]
        The array of numbers to iterate

    mu : float
        The mathematical symbol mu's value in the formula

    Returns
    -------
    float[]
        The array of numbers after applying the formula for each
    """

    print("Applying formula to generated numbers ...")

    test = -(1 / mu) * np.log(1 - numbers)

    print("Done.\n\n")

    return test


def plot_histogram(data):
    """
    Plots a given set of data.

    Parameters
    ----------
    data : int[]
        The array of numbers to plot
    """

    print("Plotting generated data...\n\n")

    plt.figure(figsize=(12, 10), dpi=80)
    plt.grid(axis='y', alpha=0.75)

    plt.title('f(p) = -(1 / mu) * ln(p)')

    n, bins, patches = plt.hist(data, bins=100, color='skyblue', alpha=0.7, rwidth=0.95)

    max_value = n.max()
    plt.ylim(ymax=np.ceil(max_value / 10) * 12 if max_value % 10 else max_value + 10)

    plt.show()

    print("Done.\n\n")


def examine_data(data, mu):
    """
    Examines a given set of data.

    Parameters
    ----------
    data : int[]
        The array of numbers to examine

    mu: float
        The value of the symbol mu in our formula
    """

    print("Examining generated data...\n")

    mean = data.mean()
    mean_one = mu * mean

    variance = data.var()
    variance_one = mu * mu * variance

    print(f"Mean value of the generated data: {mean}\n")
    print(f"Mu times mean: {mean_one}\n")
    print(f"Variance of the generated data: {variance}\n")
    print(f"Mu times mu times variance: {variance_one}\n")

    print("Done.\n\n")


def main():
    """
    Main function.

    Called on script execution
    """

    quantity = 1000000
    mu = 0.15

    random_numbers = generate_random_numbers_uniform(quantity)
    data = iterate_formula(random_numbers, mu)
    examine_data(data, mu)
    plot_histogram(data)


if __name__ == "__main__":
    main()
