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
from Sorts_List_linked import Sorts
from List_linked import List

a = List()

b = [99, 50, 2, 5, 880, 12, 15, 2]

for n in b:
    a.append(n)
    

print("Unsorted: {}".format([x for x in a]))

Sorts.radix_sort(a)

print("Sorted: {}".format([x for x in a]))