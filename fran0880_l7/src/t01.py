'''
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matthew Francis
ID:      180920880    
Email:   fran0880@mylaurier.ca
__updated__ = "2019-03-04"
-------------------------------------------------------
'''
from List_linked import List

lst = List()
lst2 = List()


for val in [1, 2, 3, 4]:
    lst.append(val)
    
_, _, i = lst._linear_search_r(1)

print(i)

_, _, i = lst._linear_search_r(2)
 
print(i)
 
_, _, i = lst._linear_search_r(3)
 
print(i)
