'''
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matthew Francis
ID:      180920880    
Email:   fran0880@mylaurier.ca
__updated__ = "2019-03-05"
-------------------------------------------------------
'''
from List_linked import List

lst = List()
lst2 = List()
lst3 = List()

for n in [1, 2, 3, 4]:
    lst.append(n)
    
for n in [1, 3, 5, 7]:
    lst2.append(n)

lst3.union_r(lst, lst2)

print(lst3._count)