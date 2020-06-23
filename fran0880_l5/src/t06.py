'''
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matthew Francis
ID:      180920880    
Email:   fran0880@mylaurier.ca
__updated__ = "2019-02-25"
-------------------------------------------------------
'''
from functions import bag_to_set

bag = [4, 5, 3, 4, 5, 2, 2, 4]
bag = [0,1,2,3,4]
print("Old: {}".format(bag))
print("New: {}".format(bag_to_set(bag)))