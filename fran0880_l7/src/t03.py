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


for n in [1, 2, 3]:
    lst.append(n)


target1, target2 = lst.split_alt_r() 

print(target1._front._value)
print(target2._front._value)
print(target1._front._next._value)
#print(target2._front._next._value)