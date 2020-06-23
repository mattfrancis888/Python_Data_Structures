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
from functions import shift
# string = input('Enter string: ')
read_file = open('pelee.txt', 'r', encoding= 'utf-8' )
string= ''
for line in read_file:
    string+=line
n = int(input('Enter n: '))
estring = shift(string, n)
print(estring)