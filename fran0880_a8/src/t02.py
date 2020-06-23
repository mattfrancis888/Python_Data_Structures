'''
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matthew Francis
ID:      180920880    
Email:   fran0880@mylaurier.ca
__updated__ = "2019-03-21"
-------------------------------------------------------
'''
from Letter import Letter
from functions import do_comparisons, comparison_total
from BST_linked import BST

DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

BST_1 = BST()
BST_2 = BST()
BST_3 = BST()

file_variable = open('otoos610', 'r', encoding = "utf=8")

for i in DATA1:
    x = Letter(i)
    BST_1.insert(x)

for i in DATA2:
    x = Letter(i)
    BST_2.insert(x)

for i in DATA3:
    x = Letter(i)
    BST_3.insert(x)

do_comparisons(file_variable, BST_1)
do_comparisons(file_variable, BST_2)
do_comparisons(file_variable, BST_3)

total_1 = comparison_total(BST_1)
total_2 = comparison_total(BST_2)
total_3 = comparison_total(BST_3)

print("Comparing by order: '{}'" .format(DATA1))
print("Total Comparsions: {}" .format(total_1))
print("Comparing by order: '{}'" .format(DATA2))
print("Total Comparsions: {}" .format(total_2))
print("Comparing by order: '{}'" .format(DATA3))  
print("Total Comparsions: {}" .format(total_3))