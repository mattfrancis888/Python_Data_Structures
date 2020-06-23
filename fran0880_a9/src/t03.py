'''
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matthew Francis
ID:      180920880    
Email:   fran0880@mylaurier.ca
__updated__ = "2019-03-27"
-------------------------------------------------------
'''
from functions import *
from Hash_Set_BST import Hash_Set
fv=open('miserables','r')
h=Hash_Set(20)
insert_words(fv, h)
total,max_word=comparison_total(h)
print('Using linked BST Hash_Set')
print()
print('Total comparisons: {:,}'.format(total))
print('Word with maximum comparisons: "{}": {:,}'.format(max_word.word,max_word.comparisons))
