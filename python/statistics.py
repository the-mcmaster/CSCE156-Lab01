"""
A collection statistics-related functions that operate on
lists of numbers.

Note: we've named our functions minimum(), maximum(), and sumVals()
because python already has min(), max(), and sum() functions that
are built-in.  In general, those functions should be used instead of
these (we've only done this to demonstrate basic functionality and
unit testing).
"""
import math

def minimum(values):
    """Finds and returns the minimal element in the given list
    of values.
    """
    minVal = math.inf
    for x in values:
        if x < minVal:
            minVal = x
    return minVal

def maximum(values):
    """TODO: write your own doc-string documentation here
    """
    # TODO: implement
    return

def sumVals(values):
    """TODO: write your own doc-string documentation here
    """
    # TODO: implement
    return

def mean(values):
    """Computes the mean value of the numbers in the given list
    of values.
    """
    return sum(values) / len(values)