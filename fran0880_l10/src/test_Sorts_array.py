'''
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matthew Francis
ID:      180920880    
Email:   fran0880@mylaurier.ca
__updated__ = "2019-03-25"
-------------------------------------------------------
'''

# Imports
import random
from Number import Number
from Sorts_array import Sorts

# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100  # Number of random arrays to generate.

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
    ('Bin. Ins. Sort', Sorts.binary_insert_sort),
    ('BST Sort', Sorts.bst_sort),
    ('Cocktail Sort', Sorts.cocktail_sort),
    ('Comb Sort', Sorts.comb_sort),
    ('Heap Sort', Sorts.heap_sort),
    ('Shell Sort', Sorts.shell_sort)
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted list of Number objects.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """

    values = []
    for i in range(SIZE):
        values.append(Number(i))
    return values

#Hint: when you need to sort these arrays, make copies of them and sort the copies so that you don't have to recreate them every time you want to test a sort.
def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed list of Number objects.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """

    values = []
    for i in range(SIZE-1, -1, -1): 
        values.append(Number(i))
    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        arrays - TEST lists of SIZE Number objects containing
            values between 0 and XRANGE (list of list of Number)
    -------------------------------------------------------
    """

    arrays = []
    for _ in range(TESTS):
        values = []
        for _ in range(SIZE):
            values.append(Number(random.randint(0,XRANGE)))
            
        arrays.append(values)
    return arrays


def test_sort(title, func):
    """
    -------------------------------------------------------
    Test a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of arrays in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """

    #Sorted
    Number.comparisons = 0
    Sorts.swaps = 0
    in_order = create_sorted()
    func(in_order)
    num_order = Number.comparisons
    num_order_swaps = Sorts.swaps
    
    #Reverse
    Number.comparisons = 0
    Sorts.swaps = 0
    in_reverse = create_reversed()
    func(in_reverse)
    num_reverse = Number.comparisons
    num_reverse_swaps = Sorts.swaps
    
    #Random
    Number.comparisons = 0
    Sorts.swaps = 0
    randoms = create_randoms()
    for random_list in randoms:
        func(random_list)
    num_random = Number.comparisons // TESTS
    num_random_swaps = Sorts.swaps // TESTS
    print("{:>15}{:>8}{:>9}{:>9}{:>9.0f}{:>9.0f}{:>9.0f}".format(title,num_order, num_reverse, num_random, num_order_swaps, num_reverse_swaps, num_random_swaps))
    return

    return