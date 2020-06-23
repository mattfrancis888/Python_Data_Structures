'''
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matthew Francis
ID:      180920880    
Email:   fran0880@mylaurier.ca
__updated__ = "2019-03-12"
-------------------------------------------------------
'''
from Priority_Queue_linked import Priority_Queue



l = Priority_Queue()
l2 = Priority_Queue()

l.is_empty()


i = 0

source1 = Priority_Queue()
source1.combine(l, l2)

while i < 3:
    l.insert(i)
    l.insert(i)
    l.peek()
    l.remove()
    i += 1 

for val in l:
    print(val)
l.split_alt()
l2.split_key(3)
l2.insert(3)
l2.remove()





