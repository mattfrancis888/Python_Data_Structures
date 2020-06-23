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
from Queue_circular import Queue
from utilities import circular_queue_test
from Movie_utilities import read_movies

fh = open('movies.txt', 'r')
movies_list = read_movies(fh)

max_size = len(movies_list)
print('Max size', max_size)
q = Queue(max_size)


for obj in movies_list:
    q.insert(obj)

circular_queue_test(q)