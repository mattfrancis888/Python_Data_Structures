'''
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matthew Francis
ID:      180920880    
Email:   fran0880@mylaurier.ca
__updated__ = "2019-02-04"
-------------------------------------------------------
'''

from utilities import array_to_queue
from Queue_array import Queue

source1 = [1,2,3,4]
source2  = [1,2,3,4]
queue1 = Queue()
queue2 = Queue()
array_to_queue(queue1, source1)
array_to_queue(queue2, source2)

print (queue1.is_identical(queue2))

