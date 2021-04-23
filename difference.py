#!/usr/bin/env python

"""
difference.py

Generates an array of random numbers, sorts it from lowest to highest, calculates the difference of each number in
the array to their preceding number, stores them in an array and plots the frequency of each value in the array.

* Change the quantity variable in the main function to generate more or fewer numbers
* Change the maximum_value variable in the main function to generate bigger or smaller numbers

This file can also be imported as a module and contains the following functions:

    * generate_sorted_random_numbers - Generates an array of sorted random numbers
    * generate_difference - Generates an array of the difference of numbers in a given array
    * plot_histogram - Plots a histogram
"""

__author__ = "Frederik Bußmann"

import matplotlib.pyplot as plt

import numpy as np


def generate_sorted_random_numbers(max_value, size):
    """
    Generates an array of random numbers, sorted from lowest to highest, by size and max value.

    Parameters
    ----------
    max_value : int
        The maximum value of the generated numbers

    size : int
        The quantity of numbers to generate, i.e. the size of the array

    Returns
    -------
    int[]
        The array of generated random numbers
    """

    print("Generating sorted array of " + str(size) + " random numbers between 0 and " + str(max_value) + "...\n")

    numbers = np.random.randint(max_value, size=size)
    numbers = np.sort(numbers)

    print("Done.\n\n")

    return numbers


def generate_difference(numbers):
    """
    Generates an array of the difference of each number in a given array to their predecessor.

    Parameters
    ----------
    numbers : int[]
        The array of numbers to iterate

    Returns
    -------
    int[]
        The array of differences of the given numbers
    """

    print("Generating array of the difference of each number to their predecessor...\n")

    difference = np.empty(numbers.size - 1, dtype=int)

    for i in range(difference.size):
        difference[i] = abs(numbers[i + 1] - numbers[i])

    print("Done.\n\n")

    return difference


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

    plt.xlabel('Difference')
    plt.ylabel('Frequency')

    plt.title('Difference between each generated value by frequency')

    _, counts = np.unique(data, return_counts=True)
    n, bins, patches = plt.hist(data, bins=len(counts), color='skyblue', alpha=0.7, rwidth=0.95)

    max_frequency = n.max()
    plt.ylim(ymax=np.ceil(max_frequency / 10) * 12 if max_frequency % 10 else max_frequency + 10)

    plt.show()

    print("Done.\n\n")


def main():
    """
    Main function.

    Called on script execution
    """

    maximum_value = 10000000
    quantity = 1000000

    random_numbers = generate_sorted_random_numbers(maximum_value, quantity)
    numbers_difference = generate_difference(random_numbers)

    plot_histogram(numbers_difference)


if __name__ == "__main__":
    main()
