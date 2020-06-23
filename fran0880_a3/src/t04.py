'''
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matthew Francis
ID:      180920880    
Email:   fran0880@mylaurier.ca
__updated__ = "2019-01-31"
-------------------------------------------------------
'''
from Stack_array import Stack

target = Stack()
source1 = Stack()
source2 = Stack()

temp_list1 = [8,12,8,5]
temp_list2 = [14,9,7,1,6,3]

for val in temp_list1:
    source1.push(val) # will create a STACK OF 4,3,2,1

for val in temp_list2:
    source2.push(val)
    
print('source1 - top to bottom')
for val in source1:
    print(val)

print()
print('source2 - top to bottom')
for val in source2:
    print(val)

print()
print('combined stack')

target.combine(source1, source2)
for val in target:
    print(val)