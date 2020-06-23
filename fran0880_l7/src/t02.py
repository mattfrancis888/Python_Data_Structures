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
lst3 = List()
lst4 = List()

for n in [1, 2, 3, 4, 4, 4, 6, 6, 6, 5, 5]:
    lst.append(n)
    
for n in [1, 2, 3, 4, 4, 4, 6, 6, 6, 5, 5]:
    lst2.append(n)


print(lst.is_identical_r(lst2))

print(lst.is_identical_r(lst3))

print(lst3.is_identical_r(lst4))