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
from utilities import array_to_stack, stack_to_array
from Stack_array import Stack
from Movie_utilities import read_movies
import Movie_utilities
a = [1, 2, 3, 4, 5, 6]
s = Stack()

array_to_stack(s, a)
print(a)
print(s)

stack_to_array(s, a)
print(a)
print(s)

fv = open('movies.txt', 'r', encoding='utf-8')
read_movies(fv)