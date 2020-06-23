'''
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matthew Francis
ID:      180920880    
Email:   fran0880@mylaurier.ca
__updated__ = "2019-03-19"
-------------------------------------------------------
'''
from Movie_utilities import read_movies
from functions import hash_table
from Hash_Set_array import Hash_Set
#from Movie import *

fh=open('movies.txt','r')
movielist = read_movies(fh)
hash_table(7 , movielist)

a = Hash_Set(7)
for val in movielist:
    a.insert(val)
a.debug()
fh.close()
    
