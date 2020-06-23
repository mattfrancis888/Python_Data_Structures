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


for n in [1, 2, 3, 4]:
    lst.append(n)


print(lst._front._value)
print(lst._front._next._value)
print(lst._front._next._next._value)
print(lst._rear._value)

lst.reverse_r()

print(lst._front._value)
print(lst._front._next._value)
print(lst._front._next._next._value)
print(lst._rear._value)