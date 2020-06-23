'''
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matthew Francis
ID:      180920880    
Email:   fran0880@mylaurier.ca
__updated__ = "2019-01-31"
-------------------------------------------------------
'''
from functions import has_balanced_brackets, BALANCED, MORE_LEFT, MORE_RIGHT,MISMATCHED
string = '{]'
balanced = has_balanced_brackets(string)
if balanced == BALANCED:
    print("'{}' has balanced brackets.".format(string))
elif balanced == MORE_LEFT:
    print("'{}' has more left brackets.".format(string))
elif balanced == MORE_RIGHT:
    print("'{}' has more right brackets.".format(string))
elif balanced == MISMATCHED:
    print("'{}' is mismatched.".format(string))