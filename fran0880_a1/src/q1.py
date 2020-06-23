'''
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matthew Francis
ID:      180920880    
Email:   fran0880@mylaurier.ca
__updated__ = "2019-01-13"
-------------------------------------------------------
'''
from functions import substitute
# string = input('Enter string: ')
ciphertext = 'DAVIBROWNZCEFGHJKLMPQSTUXY'
read_file = open('pelee.txt', 'r', encoding= 'utf-8' )

string= ''
for line in read_file:
    string+=line
    
estring = substitute(string, ciphertext)
print(estring)