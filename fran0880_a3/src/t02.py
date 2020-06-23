'''
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matthew Francis
ID:      180920880    
Email:   fran0880@mylaurier.ca
__updated__ = "2019-01-30"
-------------------------------------------------------
'''
from Stack_array import Stack

source = Stack()

temp_list = [1,2,3,4]
for val in temp_list:
    source.push(val) # will create a STACK OF 4,3,2,1

print('BEFORE REVERSE - top to bottom')
for val in source:
    print(val)

print()

source.reverse()

print('AFTER REVERSE - top to bottom')
for val in source:
    print(val)