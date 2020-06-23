'''
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matthew Francis
ID:      180920880    
Email:   fran0880@mylaurier.ca
__updated__ = "2019-01-12"
-------------------------------------------------------
'''
from functions import is_leap_year
year =  int(input('Enter year: '))
leap_year = is_leap_year(year)
print(leap_year)