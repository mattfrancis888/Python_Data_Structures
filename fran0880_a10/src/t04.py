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
from Sorts_Deque_linked import Sorts
from Deque_linked import Deque

a = Deque()

b = [99, 50, 2, 5, 880, 12, 15, 2]

for n in b:
    a.insert_rear(n)
    

print("Unsorted: {}".format([x for x in a]))

Sorts.gnome_sort(a)

print("Sorted: {}".format([x for x in a]))