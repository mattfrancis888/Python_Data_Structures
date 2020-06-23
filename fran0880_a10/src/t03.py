'''
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matthew Francis
ID:      180920880    
Email:   fran0880@mylaurier.ca
__updated__ = "2019-04-03"
-------------------------------------------------------
'''
from Sorts_array import Sorts

a = [99, 50, 2, 5, 880, 12, 15, 2]

print("Unsorted: {}".format(a))

Sorts.gnome_sort(a)

print("Sorted: {}".format(a))