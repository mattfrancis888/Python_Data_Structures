'''
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matthew Francis
ID:      180920880    
Email:   fran0880@mylaurier.ca
__updated__ = "2019-01-22"
-------------------------------------------------------
'''
from Movie_utilities import get_by_year, read_movies
fv = open('movies.txt', 'r', encoding = 'utf-8')
movies = read_movies(fv)
year = 1994
for movie in get_by_year(movies, year):
    print(movie)
    print()