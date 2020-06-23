'''
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matthew Francis
ID:      180920880    
Email:   fran0880@mylaurier.ca
__updated__ = "2019-03-20"
-------------------------------------------------------
'''
from functions import letter_table, do_comparisons
from Letter import Letter
from BST_linked import BST

DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
BST_1 = BST()
file_variable = open('otoos610', 'r', encoding = "utf=8")

for i in DATA1:
    l = Letter(i)
    BST_1.insert(l)
    
do_comparisons(file_variable, BST_1)

letter_table(BST_1)
