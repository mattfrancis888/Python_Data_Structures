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
from functions import queue_is_identical
from utilities import array_to_queue
from Queue_array import Queue
queue1 = Queue()
queue2 = Queue()

source1 = [1,2,3,4]
source2  = [1,2,3,4]

array_to_queue(queue1, source1)
array_to_queue(queue2, source2)

print(queue_is_identical(queue1, queue2))