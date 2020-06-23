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
from Queue_linked import Queue



l = Queue()
l2 = Queue()

print('Is identical:')
print (l.is_identical(l2))
print()

l.is_empty()
l.is_full()


i = 0

source1 = Queue()
source1.combine(l, l2)

while i < 3:
    l.insert(i)
    l.insert(i)
    l.peek()
    i += 1 

for val in l:
    print(val)
l.split_alt()
l2.insert(3)
l2.remove()





