'''
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matthew Francis
ID:      180920880    
Email:   fran0880@mylaurier.ca
__updated__ = "2019-01-29"
-------------------------------------------------------
'''
from Priority_Queue_array import Priority_Queue
from utilities import priority_queue_test
from Movie_utilities import read_movies
a = Priority_Queue()
list =[66, 55, 44, 33, 22, 11]
for val in list:
    a.insert(val)
print(a.remove())
fv= open('movies.txt', 'r', encoding= 'utf-8')
a = read_movies(fv)
priority_queue_test(a)