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
from test_Sorts_array import test_sort, SORTS
print("n:   100       |      Comparisons       | |         Swaps          |\nAlgorithm      In Order Reversed   Random In Order Reversed   Random\n-------------- -------- -------- -------- -------- -------- --------")
for sort in SORTS:
    test_sort(sort[0],sort[1])