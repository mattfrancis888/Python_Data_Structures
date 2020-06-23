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
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue

def queue_is_identical(source1, source2):
    """
    ----------------
    Determines whether two given queues are identical. Entries of 
    source1 and source2 are compared and if all contents are identical
    and in the same order, returns True, otherwise returns False.
    Use: identical = queue_is_identical(source1, source2)
    ---------------
    Parameters:
        source1 - a queue (Queue)
        source2 - a queue (Queue)
    Returns:
        identical - True if source1 and source2 are identical, False otherwise. 
            source1 and source2 are unchanged. (boolean)
    ---------------
    """
    identical = True
    temp_queue1 = source1
    temp_queue2 = source2
    
    if not temp_queue1.is_empty() and not temp_queue2.is_empty():    
        while not temp_queue1.is_empty() and not temp_queue2.is_empty():
            if temp_queue1.peek() != temp_queue2.peek():
                identical = False
            temp_queue1.remove()
            temp_queue2.remove()
    
    return identical       
    

def pq_split_key(source, key):
    """
    -------------------------------------------------------
    Splits a priority queue into two depending on an external
    priority key. The source priority queue is empty when the method
    ends. The order of the values from source is preserved.
    Use: target1, target2 = pq_split_key(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a data object (?)
    Returns:
        target1 - a priority queue that contains all values
            with priority higher than key (Priority_Queue)
        target2 - priority queue that contains all values with
            priority lower than or equal to key (Priority_Queue)
    -------------------------------------------------------
    """
    target1 = Priority_Queue()
    target2 = Priority_Queue()
    
    while len(source) > 0:
        removed_val = source.remove()
        
        if removed_val < key:
            target1.insert(removed_val)
        else:
            target2.insert(removed_val)
    
    return target1, target2

            
