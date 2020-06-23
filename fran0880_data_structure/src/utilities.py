'''
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matthew Francis
ID:      180920880    
Email:   fran0880@mylaurier.ca
__updated__ = "2019-01-20"
-------------------------------------------------------
'''
from Stack_array import Stack
from Priority_Queue_array import Priority_Queue
from List_array import List
from Queue_circular import Queue
def stack_to_array(stack, target):

    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not stack.is_empty():
        target.insert(0, stack.pop())

 

def stack_test(source):

    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and 
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    s = Stack()
    for item in source:
        s.push(item)
    print(s.is_empty())
    print(s.pop())
    print(s.peek())

    
    

def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack, 
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for i in range(len(source)):
        stack.push(source.pop())
#QUEUES
def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue, 
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while len(source) > 0:
        queue.insert(source.pop(0))
        
    return 



def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while len(queue) > 0:
        target.append(queue.remove())
        
    

def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq, 
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue_array object (Priority_Queue_array)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) > 0:
        pq.insert(source.pop(0))

def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue_array object (Priority_Queue_array)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(pq) > 0:
        target.append(pq.remove())

def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        the methods of Queue are tested for both empty and 
        non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    -------------------------------------------------------
    """
    list =[66, 55, 44, 33, 22, 11]

    q = Queue()
    q.is_empty()
    for val in list:
        q.insert(val)
    q.remove()
    q.peek()
    q.len()

    # tests for the queue methods go here
    # print the results of the method calls and verify by hand

    return

def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Use: pq_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        the methods of Priority_Queue_array are tested for both empty and 
        non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    -------------------------------------------------------
    """
    list =[66, 55, 44, 33, 22, 11]
    pq = Priority_Queue()
    pq.is_empty()
    for val in list:
        pq.insert(val)
    pq.remove()
    pq.peek()


    # tests for the priority queue methods go here
    # print the results of the method calls and verify by hand

    return

#List
def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist, 
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) > 0:
        llist.append(source.pop(0))
    return

def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(llist) > 0:
        target.append(llist.pop(0))
    return

def list_test(a):
    """
    -------------------------------------------------------
    Tests list implementation.
    The methods of List are tested for both empty and 
    non-empty lists using the data in a:
    is_empty, insert, remove, append, index, __contains__,
    find, count, max, min, __getitem__, __setitem__
    Use: list_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()
    lst.is_empty()
    lst.insert(0 ,1)
    lst.remove(0)
    lst.append(1)
    lst.index(1)
    lst.__contains__(1)
    lst.find(1)
    lst.count(1)
    lst.max()
    lst.min()
    lst.__getitem(0)
    lst.__setitem__(0)
    
    # tests for the List methods go here
    # print the results of the method calls and verify by hand

    return

def circular_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Use: circular_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        the methods of Priority_Queue_array are tested for both empty and 
        non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    -------------------------------------------------------
    """
    print('Empty:',a.is_empty())
    print('Length:', len(a))
    print('Is full:', a.is_full())
    while not a.is_empty():
        a.peek()
        a.remove()
    return
    