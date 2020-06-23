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
from utilities import array_to_pq, pq_to_array
from Priority_Queue_array import Priority_Queue

source1 = [1,2,20,30]
queue1 = Priority_Queue()
array_to_pq(queue1, source1)
key = 10

target1, target2 = queue1.split_key(key)

sorted1=[]
sorted2=[]

pq_to_array(target1, sorted1)
pq_to_array(target2, sorted2)

print(sorted1, sorted2)

    